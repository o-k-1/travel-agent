#!/usr/bin/env bash
# Editorial harvest: scroll-and-append innerText through the paywall proxy.
# Copy into <trip>/scrape/, edit TRIP and MANIFEST, run in BACKGROUND.
#
#   Bash tool: run_in_background: true   (a 20-article harvest exceeds 2 min)
#
# Why it looks like this (each line was a bug first, see
# references/scraping-playbook.md):
#   - PROXY points at accessarticlenow, which is the IFRAME SOURCE behind
#     removepaywalls.com. Navigating to the removepaywalls URL leaves the
#     article inside an iframe that the CLI cannot hold context on between
#     invocations. Go straight to the iframe src.
#   - Galleries virtualize: only the active slide renders. Scroll and append,
#     dedupe offline. Passes: 8-10 for a story, 16-20 for a long gallery.
#   - `| tail -1` because agent-browser eval prints a status line first.
#   - `wait 2500` after networkidle because publishers hydrate late.
#   - stdout of navigation calls goes to /dev/null or CDP chatter drowns the log.

set -u
TRIP="<WORKSPACE>/YYYY-MM-DD-DESTINATION-itinerary"
cd "${TRIP}/scrape" || exit 1
mkdir -p raw

PROXY="https://accessarticlenow.com/api/c/full?q="

# slug|url|scroll_passes
MANIFEST=(
"cnt-city-restaurants|https://www.cntraveler.com/gallery/best-restaurants-in-CITY|18"
"cnt-city-things-to-do|https://www.cntraveler.com/gallery/best-things-to-do-in-CITY|16"
"cnt-city-guide|https://www.cntraveler.com/story/CITY-guide|10"
"nyt-36h-city|https://www.nytimes.com/interactive/YYYY/travel/things-to-do-CITY.html|12"
"eater-38-city|https://CITY.eater.com/maps/best-restaurants-CITY|20"
)

FAILED=()
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
  size=$(wc -c < "$out")
  echo "  -> ${size} chars"
  # under 3000 chars means the proxy served a stub, not the article
  if [ "$size" -lt 3000 ]; then
    echo "  !! SUSPECT: under 3000 chars, proxy probably failed"
    FAILED+=("$slug")
  fi
done

echo
echo "=== SUMMARY ==="
wc -c raw/*.txt
if [ ${#FAILED[@]} -gt 0 ]; then
  echo
  echo "SUSPECT FILES (try archive.ph, then Wayback, then stop and report):"
  for f in "${FAILED[@]}"; do echo "  $f"; done
fi
echo "ALL DONE"
