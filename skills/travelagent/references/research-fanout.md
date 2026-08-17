# Research Fan-Out Plan

The main thread orchestrates. Subagents do the reading. This is not optional for a real trip: the
Japan build ran six thematic research agents, four extraction agents, and three verification agents,
and the main thread stayed clean enough to hold the whole itinerary in view.

Dispatch rule from standing memory: **3 or more entities times 2 or more data products means fan
out from message one.** A multi-city trip always clears that bar.

---

## Wave 1: thematic research (parallel, one per lens)

Dispatch all of these in a single message. Each writes its own `.psv` to `research/` and returns a
short summary. Model: `sonnet` for the taste-heavy lenses, `haiku` is acceptable for date and
logistics lookups.

| Agent | Lens | Output file |
|---|---|---|
| 1 | **Dining, Track A**: awarded, cult, chef-driven, hard-to-book. Michelin, 50 Best and regional lists, local critical canon. Must return the booking platform and lead time per venue. | `research/dining-awarded.psv` |
| 2 | **Dining, Track B**: hole-in-the-wall, counters, market stalls, workers' canteens, multi-generation single-dish shops. Plus the "dishes to hunt" list of regional specialties, plus the rare-protein and game traditions if any genuinely exist. | `research/dining-local.psv` |
| 3 | **Sights and history**: temples, churches, castles, palaces, museums, memorials, districts. Each with the historical argument, UNESCO status, hours, closed day, ticketing and timed-entry rules. | `research/sights.psv` |
| 4 | **Architecture and photography**: modern and contemporary buildings with architect and year, vernacular typologies, walking routes, night and street photo locations, elevated vantage points, golden and blue hour times for the actual dates, photography restrictions. | `research/architecture-photo.psv` |
| 5 | **Menswear and textile craft**: independent labels, heritage workwear, the local dye and weave tradition and its living makers, concept stores, vintage and secondhand, mills and factory shops, tailors. Silhouette filter: wide-leg, high-waisted, pleated, textured. | `research/menswear.psv` |
| 6 | **Non-clothing retail**: hand-forged knives and the local blade tradition, ceramics and kiln regions, regional craft goods, affordable vintage watches (hundreds to low thousands USD), used cameras and lenses, books and records. Include tax-free mechanics and shipping. | `research/retail-craft.psv` |
| 7 | **Workshops and living culture**: master-led classes (dye, weave, ceramics, blades, paper, cooking), authentic ritual practice, artisan visits. Filter out staged tourist demonstrations or label them as such. | `research/workshops.psv` |
| 8 | **Active**: cycling infrastructure and routes with rental logistics, driving routes only if the destination warrants them plus the full licence and IDP chain, hikes, baths and swimming, urban walking routes. | `research/active.psv` |
| 9 | **Live sport and events**: the local spectator sport with the best crowd ritual, actual fixtures inside the trip dates, ticket mechanics, plus festivals, matsuri, processions, markets, and one-off exhibitions falling inside the dates. | `research/events.psv` |
| 10 | **Logistics and calendar**: rail and transit passes with the break-even arithmetic, IC cards, airport transfers, luggage forwarding, connectivity, cash norms, tipping, tax refund, IDP requirement and where to get it, **and the closure calendar**: public holidays, weekly closure days by venue type, seasonal road and trail closures, anything shut on specific trip dates. | `research/logistics.md` (prose, not psv) |

Prompt template for a wave-1 agent:

```
You are researching <LENS> for a <N>-day trip to <DESTINATION>, <EXACT DATES>.

TRAVELER PROFILE (do not deviate): <paste the relevant 6-10 lines from traveler-profile.md>

Return 25 to 60 records in this exact pipe-delimited format, one per line, no preamble,
no markdown fences, no header row:
city || category || subcategory || name || local_name || maps_query || neighborhood ||
cluster || hours || closed || res || res_how || price || tier || note || why || flags || source

<paste the field table and RES tag table from data-schema.md>

HARD RULES
- Every record needs an hours value. If you cannot verify hours, write "unknown, verify".
  NEVER invent hours.
- Every record needs a res tag. RES:none is a valid answer.
- Prices in local currency and USD.
- tier: mark the true must-books as anchor. For every anchor requiring a reservation stricter
  than RES:2-3d, include at least two same-cluster, same-price-band records tiered strong or
  alternate, with at least one of them RES:walk-in or RES:same-day.
- Flag anything you could not confirm is still open with verify-open.
- No hotels, no lodging, no packing advice, no out-of-season items (the trip is in <MONTH>).
- Cite your source in the source field. Real sources only.

Use WebSearch and WebFetch. Write your output with the Write tool to:
<TRIP>/research/<file>.psv
Then return a 5-line summary: count, the 3 strongest finds, and anything you could not verify.
```

## Wave 2: editorial harvest (parallel, one per source family)

Runs concurrently with wave 1; it does not depend on it.

1. Main thread builds the article manifest (see `source-catalog.md` for how to find articles per
   publisher, and ask the traveler if they have specific URLs, as they did for the Japan build).
2. Main thread runs the harvest script as one background bash job (`scraping-playbook.md`).
3. One extraction subagent **per city bucket**, not per article, over the clean text.

Buckets for a typical trip: `<city1>`, `<city2>`, `<city3+other>`, `daytrips`.

## Wave 3: verification (parallel, after waves 1 and 2 merge)

Cheap, high-value, and the step most often skipped. Model `haiku` is fine.

| Agent | Checks |
|---|---|
| A | **Still-open sweep.** Every record flagged `verify-open` plus every record whose source is a single listicle. Confirm the venue exists, is open, and has not moved. The Japan build caught six stale entries this way: a demolished tower, a museum under renovation, a market that relocated in 2018, an attraction that moved buildings in 2024, and two permanent closures. |
| B | **Hours and closed-day sweep.** For every anchor, confirm hours and weekly closure against the official site. Then cross the trip dates against them and produce a per-date "what is closed today" list. |
| C | **Reservation reality check.** For every record with a res tag stricter than `RES:2-3d`, confirm the platform still handles it, whether a local phone or card is required, and when the booking window opens. Produce the reservation tracker rows. |
| D | **Date collision check.** Cross every dated item (fixtures, festivals, markets, exhibitions, holidays) against the itinerary and surface every conflict. Do this before writing the day-by-day, not after. |

## Wave 4: build (main thread, no subagents)

Run the build scripts. The main thread owns document assembly because it is the only context that
holds the whole plan.

---

## Anti-patterns

- **Do not fan out what a 30-second command answers.** Standing memory: before spawning parallel
  agents, ask whether a single bash command or a single fetch would do it.
- **Do not let raw tool output reach the main thread.** A wave-1 agent that returns 60 records of
  prose commentary instead of 60 psv lines has failed. Filter in the subagent.
- **Do not pull data without a question attached.** "Research Kyoto" is a bad prompt. "Find the
  Higashiyama temple cluster in walking order with hours and closed days" is a good one.
- **Do not run wave 3 as one agent.** Four narrow checkers beat one broad one, and they run in
  parallel.
- **Do not skip wave 3 because wave 1 looked confident.** Confidence is not verification.
