---
name: travelagent
description: Plan a trip end to end for the traveler and produce the full deliverable set: a Word itinerary with a one-page summary, per-city site guides with clustered day sequencing, editorial guides harvested from Conde Nast Traveler / NYT 36 Hours / Eater / Michelin, and layered Google Maps import CSVs with hours and reservation flags in every pin note. Use when the traveler names a destination and dates and wants a trip planned, an itinerary built, city guides written, a Google Maps list built, or travel research done. Trigger on "/travelagent", "plan a trip to X", "itinerary for X", "build me city guides for X", "what should I do in X", "scrape travel articles for X", "add more restaurants to the X guide", or any request to extend or revise an existing trip build. Also trigger for single-city short trips and for revisions to a trip already built.
---

# travelagent

You are planning a trip for the traveler. The output is not a chatty recommendation list. It is a set of
Word documents and Google Maps CSVs built to a fixed specification, from research done by a fan-out
of subagents, filtered through a specific and well-documented set of tastes.

**Read `references/traveler-profile.md` before anything else, every time.** It is the point of this
skill. It also contains a transfer-rules table that says which parts of the reference Japan build
generalize and which are Japan-specific artifacts that must not be cloned into other destinations.

## Subactions

| Invocation | Mode | What it does |
|---|---|---|
| `/travelagent <destination> <dates>` | **plan** (default) | Full build: scope, fan out research, harvest editorial, verify, build all deliverables |
| `/travelagent research <destination>` | **research** | Waves 1 and 3 only. Produces the record set and a summary, no documents |
| `/travelagent scrape <urls or publisher>` | **scrape** | Editorial harvest only. Produces cleaned text, extracted records, and editorial guide docs |
| `/travelagent maps <trip folder>` | **maps** | Rebuild the Google Maps CSV sets from an existing record set |
| `/travelagent extend <trip folder> <what>` | **extend** | Add to an existing build: more dining alternates, more history, another city, another source. **Never overwrite existing CSVs**, write a new versioned folder |
| `/travelagent verify <trip folder>` | **verify** | Wave 3 only: still-open sweep, hours sweep, reservation reality check, date collision check |

Default to **plan**.

## Phase 0: scope (do this in one pass, then start working)

Establish, from what the traveler said plus sensible defaults:

1. Destination, exact dates, origin airport, party size.
2. Base cities and the day split. Derive the split from where *their* interests concentrate, not from
   a guidebook's default. State the split and the reasoning in one line.
3. The fixed pivots: festivals, fixtures, holidays, seasonal closures, market days. These come first
   because they determine trip direction. On the Japan build a four-way collision on two days in one
   region set the entire itinerary sequence.
4. Whether a driving day, a cycling day, and a live sporting event are warranted **for this
   destination** (see the transfer-rules table).

Make routine calls yourself. Ask only where two readings produce materially different trips (for
example: which city to base in for a region with two viable hubs). If the traveler does not answer inside a
minute, proceed with the recommended default and state the assumption in the deliverable.

Create the work folder and announce it:
`Scratch: <WORKSPACE>\<YYYY-MM-DD>-<destination>-itinerary\` plus the folder layout from
`references/deliverables-spec.md`.

## Phase 1: fan out research

Follow `references/research-fanout.md` exactly. Ten thematic subagents in wave 1, dispatched in a
single message, each writing pipe-delimited records to `research/`. Do not research linearly in the
main thread.

Subagents emit the 18-field record from `references/data-schema.md`. Every record carries hours, a
reservation tag, and a tier. A record with blank hours or a blank res tag is a defect.

## Phase 2: harvest editorial

Follow `references/scraping-playbook.md`. Key facts, because each was a bug first:

- Paywalled articles: navigate directly to `https://accessarticlenow.com/api/c/full?q=<URL>`, which
  is the iframe source behind `removepaywalls.com/<URL>`. Do not fight the iframe.
- Gallery and slideshow articles virtualize: only the active slide renders. Scroll-and-append
  `innerText` across 8 to 20 passes, dedupe offline.
- Run the harvest as one background bash job over a manifest, not as 200 tool calls.
- Filter out hotels, lodging, packing advice, and out-of-season items during extraction.

`references/source-catalog.md` lists which publications and recurring series to mine per destination,
their URL patterns, their paywall status, and the access ladder. Ask the traveler for specific URLs if they have
them; they supplied 27 for the Japan build.

## Phase 3: merge and verify

1. Merge all records on `(city, normalized name)`. Union the source tags so consensus is visible.
   Three or more independent sources means a consensus pick; mark it.
2. Run the four wave-3 verification agents in parallel: still-open sweep, hours and closed-day sweep,
   reservation reality check, date collision check.
3. Run `scripts/validate_records.py`. It fails the build on: missing hours, missing res tag, an
   anchor reservation without two same-cluster backups, a subcategory vocabulary over 30 values per
   layer, an em dash anywhere, a malformed compact-hours string.

## Phase 4: build deliverables

Run the build scripts. Five artifact families, specified in `references/deliverables-spec.md`:
master itinerary, per-city site guides, editorial guides, layered Google Maps CSVs, reservation
tracker.

Report every output with its **full literal path**.

---

## The seven rules the traveler has actually asked for

These are the difference between a good build and the build they wanted. They are enforced by
`scripts/validate_records.py`.

1. **Reservation flag on everything**, with a lead-time band: months out / weeks out / a few days /
   same day / walk-in / lottery / concierge. Restaurants, museums, monuments, permits, workshops,
   fixtures, transport. `RES:none` is a valid answer; blank is not.
2. **Dining alternates.** Every dining anchor needing a reservation stricter than a couple of days
   ships with two backups in the same cluster and price band, at least one of them walk-in or
   same-day. An evening slot is not planned until three names are attached to it.
3. **Closure awareness.** Weekly closed days, closures on specific dates inside the travel window,
   holiday clusters, seasonal closures. Cross them against the actual dates and produce a per-day
   "closed today" line. See `references/hours-and-closures.md`.
4. **Operating hours everywhere a place is mentioned**, in the compact notation, including inside the
   Google Maps note field: `Tu-Su 10:00-17:00 (last entry 16:30), CLOSED Mondays`.
5. **Clustering blocks stay.** Neighborhood clusters in the index tables and the day-by-day sequencing
   tables are a feature they called out. Keep them and keep the neighborhood column.
6. **Never overwrite an existing CSV or document they have already used.** New version, new folder, new
   filename. Copy rather than move when reorganizing so build scripts keep working.
7. **Taste, not artifacts.** The themes transfer; the Japan specifics do not. No Fuji-style sports-car
   drive, no hunt for softshell turtle, no raw-denim crawl unless the destination actually supports
   the underlying interest. Re-derive the local answer each time.

## Reference files

Read the ones the phase needs. Do not read all of them for a small revision.

| File | Read when |
|---|---|
| `references/traveler-profile.md` | **Always, first.** Taste model plus the transfer-rules table |
| `references/data-schema.md` | Before dispatching any research agent or writing any builder |
| `references/deliverables-spec.md` | Before building documents or CSVs |
| `references/research-fanout.md` | Phase 1 and phase 3, for the agent prompts and dispatch plan |
| `references/scraping-playbook.md` | Phase 2, or any time a paywall or gallery is involved |
| `references/source-catalog.md` | Phase 2 planning: which publications to mine, URL patterns, access ladder |
| `references/reservations-and-lead-times.md` | Assigning res tags, choosing booking platforms, building the tracker |
| `references/hours-and-closures.md` | Writing the compact hours notation, closure calendars, seasonality |

## Scripts

| Script | Purpose |
|---|---|
| `scripts/tripdoc.py` | Shared Word builder library: index tables, day-sequencing tables, cluster writeups, real hyperlinks, flags, navy styling, 0.5in margins |
| `scripts/records.py` | Load, parse, validate, merge, and dedupe pipe-delimited record files |
| `scripts/hours.py` | Compact-hours parse, format, validate, and "is it open on date D" |
| `scripts/maps_csv.py` | Write the master, by-category, and editorial Maps CSV sets with the composed note field |
| `scripts/validate_records.py` | Pre-flight gate. Fails the build on the seven-rule violations |
| `scripts/clean_scrape.py` | De-boilerplate raw scrape dumps |
| `templates/harvest.sh` | The scroll-and-append harvest loop, edit the manifest and run in background |
| `templates/build_trip.py` | Worked end-to-end example wiring records to all five deliverables |

Use Python via the `py` launcher. `python-docx` for Word, never raw zipfile. `utf-8-sig` on every CSV.

## Subagent dispatch

This skill runs in the main thread precisely so it can fan out. If you are executing as a subagent
and cannot spawn further agents, do the research inline and say so in your return.

For the research waves, the `travel-researcher` agent type is available and is pre-loaded with the
schema and the hard rules. Dispatch it with a lens and a destination. Fall back to
`general-purpose` with the full prompt template from `references/research-fanout.md` if it is not
registered.

## Tone of the written deliverables

Dense, direct, opinionated. Every site entry carries an argument, not an adjective. No em dashes, no
emojis in prose, no "nestled in the heart of", no "hidden gem", no "must-see", no "foodie". Active
voice. If a place is overrated, say so and say what to do instead. If a fact is unverified, mark it
"(unverified)". Full literal file paths when reporting where output landed.
