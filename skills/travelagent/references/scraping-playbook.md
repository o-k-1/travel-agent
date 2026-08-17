# Scraping Playbook

Operational recipes for harvesting travel editorial. Everything here was verified on the Japan build
(27 Conde Nast Traveler articles, about 2.7 MB raw to about 300 KB clean to 353 extracted places).

Tool of choice: **`agent-browser`** CLI (drives Chrome over CDP). Prefer it over the Playwright MCP
for bulk harvesting because each call is a cheap shell invocation and the loop is scriptable in bash,
so 20 articles cost one background job instead of 200 tool calls.

---

## 1. The paywall proxy: the one detail that matters

`https://removepaywalls.com/<FULL-ARTICLE-URL>` works, but it renders the article **inside an
iframe**. Two failures follow from that:

1. `agent-browser eval "document.body.innerText"` on the outer page returns about 160 characters of
   chrome, not the article.
2. `agent-browser frame "iframe"` returns "Frame not found". `frame @e2` (a snapshot ref) does attach,
   but **frame context does not persist between CLI invocations**, so the next `eval` is back on the
   outer document.

**The fix: read the iframe's `src` and navigate straight to it.** The iframe src is:

```
https://accessarticlenow.com/api/c/full?q=<FULL-ARTICLE-URL>
```

Navigating directly to that URL puts the article text in the top-level document, where `innerText`
works. This turned 163 characters into 5,338 characters of real content on the first test.

```bash
PROXY="https://accessarticlenow.com/api/c/full?q="
agent-browser open "${PROXY}${ARTICLE_URL}"
agent-browser wait --load networkidle
agent-browser eval "document.body.innerText"
```

If `accessarticlenow` changes shape, re-derive it: open the removepaywalls URL, `agent-browser
snapshot -i`, find the iframe ref, then `agent-browser get attr <ref> src`. Do not go back to
fighting the frame context.

Fallback order when the proxy fails: `archive.ph/<url>`, then Wayback
(`web.archive.org/web/2/<url>`), then the publisher's own free-article allowance, then ask the traveler
whether they have a subscription or library access for that title. Two failures on the same article,
then move on and log the gap rather than looping. See `source-catalog.md` for the full access ladder.

## 2. Gallery virtualization: the second trap

Slideshow and gallery articles (`cntraveler.com/gallery/...` and most "best X" listicles) **only
render the active slide's text in the DOM**. Consequences:

- A single `innerText` grab returns 2 of 25 venues.
- An accumulator harvester that hooks a `window.__H` array and listens for slide changes collected
  only 7 of 25. Do not bother.
- There is no embedded preloaded JSON to mine. On the Japan build `document.scripts.length` was 1 and
  it held nothing useful.

**The fix: scroll and append.** Grab `innerText`, scroll a fixed amount, wait, grab again, N times.
Duplicated text is fine; dedupe offline. Pass count by article length: 8 to 10 for a standard story,
16 to 20 for a long gallery.

Validate coverage by counting a repeated per-item marker in the raw dump. CNT galleries repeat
"Read Full Review" once per venue, so `grep -c "Read Full Review"` against the expected item count
tells you whether the scroll passes were sufficient. Find the equivalent marker for other publishers
(a rating badge, "Book now", an address line) before trusting a harvest.

## 3. The harvest script pattern

Write it to a file and run it as one background job. Do not drive 20 articles through 200 individual
tool calls.

```bash
#!/usr/bin/env bash
cd "<TRIP>/scrape" || exit 1
mkdir -p raw
PROXY="https://accessarticlenow.com/api/c/full?q="
# slug|url|scroll_passes
MANIFEST=(
"tokyo-restaurants|https://www.cntraveler.com/gallery/best-restaurants-in-tokyo|18"
"kyoto-things-to-do|https://www.cntraveler.com/gallery/best-things-to-do-in-kyoto|16"
"36h-tokyo|https://www.nytimes.com/interactive/2024/travel/things-to-do-tokyo.html|10"
)
for entry in "${MANIFEST[@]}"; do
  IFS='|' read -r slug url passes <<< "$entry"
  out="raw/${slug}.txt"
  echo "=== $slug ($passes passes) ==="
  agent-browser open "${PROXY}${url}" >/dev/null 2>&1
  agent-browser wait --load networkidle >/dev/null 2>&1
  agent-browser wait 2500 >/dev/null 2>&1
  : > "$out"
  echo "URL: $url" >> "$out"
  for i in $(seq 1 "$passes"); do
    agent-browser eval "document.body.innerText" 2>/dev/null | tail -1 >> "$out"
    agent-browser scroll down 1400 >/dev/null 2>&1
    agent-browser wait 350 >/dev/null 2>&1
  done
  echo "  -> $(wc -c < "$out") chars"
done
echo "ALL DONE"
```

Notes on the details, each of which was a bug first:

- `| tail -1` because `agent-browser eval` prints a status line before the value.
- `wait 2500` after networkidle: CNT hydrates late and networkidle fires early.
- `>/dev/null 2>&1` on navigation calls or the log drowns in CDP chatter.
- Run with `run_in_background: true`. A 25-article harvest exceeds the 2-minute Bash timeout. Do not
  poll with `sleep` loops longer than 115 seconds; rely on the completion notification.

## 4. Cleaning

`clean.py` over `raw/*.txt` to `clean/*.txt`:

1. Unescape `\n` sequences that `eval` returns literally.
2. Drop lines matching a `BOILER` list: nav items, "Sign In", "Subscribe", "Read More", social
   labels, footer legal, cookie text, newsletter prompts, "Advertisement". Build this list by
   eyeballing one raw file; it is publisher-specific and takes two minutes.
3. Drop ALL-CAPS lines under 40 characters (section labels and nav).
4. Dedupe paragraphs by exact match, preserving first-seen order.

Expect roughly a 90 percent size reduction. Verify the clean file still contains the per-item marker
count from step 2 before extracting.

## 5. Extraction

Fan out one extraction subagent per city bucket (not per article) over the clean files. Give each:

- the list of clean file paths for its bucket,
- the full 18-field schema from `data-schema.md`,
- the exclusion filter (no hotels, no lodging, no packing advice, no out-of-season items, no generic
  "walk around and soak up the atmosphere" entries),
- the instruction to emit ` || ` lines only, no preamble, no markdown fences,
- the instruction to write directly to `research/<bucket>.psv` with the Write tool,
- an explicit "if the article does not state hours, write `unknown, verify`; never invent hours"
  instruction.

Then parse the `.psv` files in the build script with a strict field-count check and log dropped lines.

## 6. Non-editorial sources worth scripting

| Source | Method |
|---|---|
| UNESCO World Heritage list for a country | `whc.unesco.org` browse-by-country page, straight fetch, no paywall |
| Michelin Guide | `guide.michelin.com` city pages, filterable by distinction; renders server-side, straight fetch usually works |
| Local booking platforms | Do not scrape; use them to confirm a venue exists and to read the booking-window rule |
| Google Maps hours | Do not scrape Maps. Fetch the venue's own site, or mark `unknown, verify`. |
| Sport schedules | The league's own site. Verify the fixture falls inside the trip dates; this is a common silent error. |
| Festival dates | The municipal or shrine/church official page, not aggregator blogs. Aggregators recycle last year's dates. |

## 7. Failure discipline

- Two identical failures on the same target, stop. Log the gap in the deliverable's assumptions
  section, tell the traveler which article or venue could not be verified, and move on.
- Never silently substitute a different source for a named one. If the traveler named an article and it is
  unreachable, try one fallback, then surface it.
- Every claim that came out of a scrape and was not cross-checked gets `verify-open` in `flags` if it
  is a venue, or "(unverified)" in prose if it is a fact.
