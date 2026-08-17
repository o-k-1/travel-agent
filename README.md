# travel-agent

A Claude Code plugin that plans a trip end to end and ships the artifacts you actually use on the
ground: a Word itinerary, per-city site guides with clustered day sequencing, editorial guides mined
from the travel press, and Google Maps import CSVs where **every pin carries its opening hours, its
reservation lead time, and its closed days**.

It is not a chatbot that lists restaurants. It is a research pipeline with a document build at the end.

```
scope -> fan out ~10 research subagents -> harvest editorial -> verify -> build 5 artifact families
```

## What it produces

| Artifact | Detail |
|---|---|
| Master itinerary (`.docx`) | One-page at-a-glance calendar, fixed pivots and date collisions, booking actions grouped by deadline, logistics, day-by-day, dining and retail master lists |
| Per-city site guide (`.docx`) | Site index table grouped by type with a neighborhood column, a day-by-day sequencing table with a "closed today" column, then per-cluster writeups carrying the historical argument |
| Editorial guide (`.docx`) | One per source family per city: summary and coverage outline, index table, the picks, and a consensus section for places corroborated by three or more independent sources |
| Google Maps CSVs | Three sets (master, by-category, editorial) sized for My Maps layer limits, with per-type icons via style-by-data |
| Reservation tracker (`.docx`) | Sorted by deadline, with a backup for every anchor that could fall through |

Every site name in every table is a live Google Maps hyperlink.

## Why the hours and reservation handling is the point

Most generated itineraries fall apart on contact with reality: the museum is shut on Monday, the
counter needed a booking six weeks ago, the market closed at noon. This plugin treats those as
first-class data rather than prose afterthoughts.

- **A compact hours notation** with a real parser (`scripts/hours.py`): `Tu-Su 10:00-17:00 (last
  entry 16:30); CLOSED M`. It validates, normalizes, and answers "is this open on date D", so each
  day of the plan can be checked against what is actually shut.
- **Ten reservation lead-time tags** from `RES:3-6mo` down to `RES:walk-in`, plus `RES:lottery` and
  `RES:concierge`. Never blank; `RES:none` is the explicit "just show up" value.
- **An enforced backup rule.** Every dining anchor needing more than a couple of days' notice must
  ship with two same-cluster fallbacks: one price peer, and one zero-risk walk-in. The build fails if
  it does not hold. A dinner slot is not planned until three names are attached to it.
- **Closure awareness** against the actual travel dates: weekly closed days, date-specific closures,
  holiday clusters, and seasonal windows.

The Maps pin note composes all of it into one line:

```
Omakase | Tu-Sa 18:00-22:00 (LO 20:30); CLOSED M, Su | RES 1-2mo ahead via Pocket Concierge
       | Edomae counter, warm aggressively vinegared shari, no ordering | Y30,000-35,000 / $200-235
```

## Install

**As a plugin** (recommended). In Claude Code:

```
/plugin marketplace add o-k-1/travel-agent
/plugin install travel-agent
```

**Manually**, if you prefer not to use the plugin system:

```bash
git clone https://github.com/o-k-1/travel-agent
cp -r travel-agent/skills/travelagent ~/.claude/skills/
cp travel-agent/agents/travel-researcher.md ~/.claude/agents/
```

Python dependency for the document builders:

```bash
pip install python-docx
```

## Use

```
/travelagent Lisbon and Porto, 10 days, October 3-13
/travelagent research Oaxaca
/travelagent scrape https://www.cntraveler.com/gallery/best-restaurants-in-mexico-city
/travelagent maps <trip folder>
/travelagent extend <trip folder> more dining alternates in Alfama
/travelagent verify <trip folder>
```

`plan` is the default. `extend` never overwrites an existing CSV; it writes a new versioned folder.

## Make it yours: replace the traveler profile

`skills/travelagent/references/traveler-profile.md` encodes one specific traveler's taste, and it is
the file that determines whether the output is any good. **Fork the repo and rewrite it.** The
profile that ships is deliberately opinionated so you can see the shape:

- high-density active pace, no resort decompression, no lodging recommendations
- a historical argument per site rather than adjectives
- modern and vernacular architecture, both, with a walking route per city
- street and night photography as a planning lens
- dual-track dining: the awarded and cult rooms weighted equally against hole-in-the-wall counters,
  organized around regional dishes that are hard to eat elsewhere
- heritage textile and craft retail as a major axis, not an afterthought
- master-led workshops over staged demonstrations
- one live local spectator sport for the crowd ritual

That file also carries a **transfer-rules table**, which is the most reusable idea in this repo. It
separates the traveler's durable preferences from the destination-specific artifacts a previous trip
happened to produce, so a Japan build does not clone a Mt. Fuji driving day into Portugal. Keep that
section when you rewrite the profile.

## How the research works

`references/research-fanout.md` defines ten parallel research lenses (awarded dining, local dining,
sights and history, architecture and photography, menswear and textile craft, non-clothing retail,
workshops, active, events and sport, logistics and calendar), then four narrow verification agents
(still-open sweep, hours sweep, reservation reality check, date collision check).

Subagents return **pipe-delimited (` || `) records with a strict 18-field count**, not CSV and not
JSON. LLM-emitted CSV shifts columns on embedded commas; one malformed JSON record kills the whole
parse. A bad pipe-delimited line costs one place and gets logged.

Editorial harvesting is documented in `references/scraping-playbook.md`, including the two traps that
cost real time: paywall proxies that render into an iframe whose context resets between CLI calls,
and gallery articles that virtualize so only the active slide is in the DOM.

## Repo layout

```
.claude-plugin/
  plugin.json               plugin manifest
  marketplace.json          so the repo can be added as a marketplace directly
agents/
  travel-researcher.md      the research subagent the skill dispatches
skills/travelagent/
  SKILL.md                  orchestrator: 6 subactions, 4 phases, the hard rules
  references/
    traveler-profile.md     taste model + transfer rules      <- rewrite this
    data-schema.md          the 18-field record
    deliverables-spec.md    the 5 artifacts, folder layout, formatting invariants
    research-fanout.md      lenses, verification agents, prompt templates
    scraping-playbook.md    browser automation recipes and traps
    source-catalog.md       ~80 sources, URL patterns, paywall access ladder
    reservations-and-lead-times.md
    hours-and-closures.md   the notation, closure patterns, holiday clusters
  scripts/
    hours.py                compact-hours parse / validate / is-open-on-date
    records.py              load, merge, dedupe, query, backup-rule check
    maps_csv.py             the three Maps CSV sets
    tripdoc.py              shared Word builder
    validate_records.py     pre-flight gate
    clean_scrape.py         de-boilerplate raw scrape dumps
  templates/
    harvest.sh              scroll-and-append harvest loop
    build_trip.py           worked end-to-end build
```

## Verify it works

```bash
python skills/travelagent/scripts/hours.py            # 19 notation forms + 5 malformed cases
python skills/travelagent/templates/build_trip.py --demo   # builds all 5 artifacts from a fixture
```

## Design decisions worth knowing

1. **The orchestrator is a skill, not a subagent.** Subagents cannot spawn subagents, and the fan-out
   is what makes this work. The skill runs in the main thread and dispatches `travel-researcher`.
2. **One record schema drives everything.** Documents and CSVs read the same 18 fields, so there is no
   translation layer to drift.
3. **The zero-risk dining backup ignores price band.** A cheap standing counter is a valid fallback
   for a splurge tasting menu even though it is nothing like a price peer. Requiring the fallback to
   match the price band was the first version of the rule and it was wrong.
4. **Hours are never invented.** A researcher that cannot verify hours writes `unknown, verify`, and
   the validator surfaces it. A plausible guess is worse than an admitted gap.
5. **Never overwrite a CSV the user has already imported.** New version, new folder.

## Caveats

- Geocoding runs off a text query and is imperfect for small owner-operated venues. Spot-check pins
  flagged `verify-open`.
- Google Maps hours are frequently stale for small venues; the hours in these outputs come from the
  source that was checked, which is why the pipeline prefers official sites.
- Google My Maps caps at 10 layers per map, 2,000 features per layer, and roughly 30 style-by-data
  groups per layer. The CSV sets are shaped around those limits.
- Scraping is subject to the terms of the sites involved. Prefer a subscription or library access you
  already hold.

## License

MIT. See `LICENSE`.
