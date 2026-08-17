# Deliverables Specification

The golden-state output set from the Japan build, generalized. Five artifact families. Produce them
in this order, because each feeds the next.

```
1. Master itinerary        .docx   one per trip
2. City site guides        .docx   one per base city (plus one for day trips)
3. Editorial guides        .docx   one per source family, per city
4. Google Maps CSVs        .csv    layered for import
5. Reservation tracker     .docx or .xlsx   the action list
```

---

## Output folder layout

Working folder: `<WORKSPACE>\YYYY-MM-DD-<destination>-itinerary\`

```
<trip folder>/
  README.md                          purpose + final destination, one line
  <YYYY.MM.DD> <Destination> Itinerary.docx
  <YYYY.MM> <City> Sites Guide.docx           one per city
  <Source> Guide - <City>.docx                e.g. "CNT Guide - Tokyo.docx"
  <YYYY.MM.DD> Reservation Tracker.docx
  MAPS - Master/                     <- the one to actually import; per-city, all categories
  MAPS - By Category/                <- granular, per city x category, for icon control
  MAPS - Editorial/                  <- source-specific sets (CNT, NYT, Eater)
  scripts/                           build scripts, one per artifact family
  research/                          subagent .psv output, raw
  scrape/
    raw/                             raw innerText dumps
    clean/                           de-boilerplated text
    records/                         extracted .psv
  intermediates/                     verification dumps, link checks
  archive/                           superseded versions
```

**Rule learned the hard way: never rewrite a CSV in place once the user has imported it.** New
versions go to new folders with a version suffix (`MAPS - Master v2/`). The traveler said this twice. Copy,
do not move, when reorganizing, so build scripts keep working.

Final deliverables stay in the trip working folder unless the traveler asks for them
somewhere else. Always report the full literal path of every output.

---

## 1. Master itinerary (.docx)

Structure, in order:

1. **One-page at-a-glance calendar.** A table: Date / Day / Base city / Theme / Anchor / Evening /
   Booked?. Must fit on one page. This is the page the traveler actually looks at.
2. **Fixed pivots and collisions.** The 3 to 6 immovable facts that shape the whole trip: a festival
   date, a match date, a market's closed day, a holiday, a road's seasonal closure. Explain the
   collision and the resolution. On the Japan build this was the July 24-25 Kansai pile-up (Gion Ato
   procession, Tigers at Koshien, Tenjin Matsuri, and conflicting Tokyo fireworks) and it determined
   the entire trip direction.
3. **Booking actions by deadline.** Grouped by lead time band: book now / book on ticketing / book 1
   month out / book 2 weeks out / book on arrival. Each line: what, where, how, cost, what happens if
   it fails.
4. **Logistics.** Arrival and transfer, rail passes and whether they pay off (do the arithmetic),
   IC cards, luggage forwarding, connectivity, cash versus card, IDP if driving, tipping, tax refund.
5. **Day-by-day.** Per day: date, base, theme, then bullets and sub-bullets for morning / midday /
   late afternoon / evening. Every venue line carries hours, RES tag, and price. Every dinner slot
   carries anchor plus two alternates.
6. **Dining master list.** Grouped by city then by dish or genre. Table columns: Place / Genre /
   Neighborhood / Hours / RES / Price / Note.
7. **Retail and craft master list.** Grouped by city then by category. Same column shape plus what
   to buy there.
8. **Seasonality and what is in season** for the exact dates.
9. **Reservation tracker.** The same actions as section 3, reformatted as a checklist with columns
   for Booked / Confirmation number / Notes.
10. **Assumptions and open questions.** Anything decided without confirmation, stated plainly.

Formatting: Calibri, 0.5 inch margins on all four sides, navy headings, bullets and sub-bullets, real
hyperlinks (not raw URLs in text), price ranges in local currency and USD.

## 2. City site guide (.docx)

One per base city plus one for day trips. Structure, in order, with page breaks between:

1. **Site index table, grouped by type.** Columns: Type / Site / Neighborhood / Hours / RES.
   Rows colour-banded by type. The site name is a **live Google Maps hyperlink**. This table is the
   proximity-planning tool, which is why the neighborhood column is mandatory.
2. **Suggested day-by-day sequence table.** Columns: Day and theme / Morning / Midday / Late
   afternoon / Evening. Ordered so travel between stops is minimal and so each day's stops are
   actually open that day. The traveler explicitly liked these clustering blocks. Keep them, and add a
   "closed today" note per day.
3. **Detailed guide, grouped by geographic cluster.** Per site: name, type, neighborhood, hours, RES
   tag, price, Maps link, then the 60 to 180 word historical or architectural argument. Flags
   (UNESCO, verify-open, no-photography) rendered in red.
4. **Closing flags.** Booking-required list, closure calendar for the trip dates, photography
   restrictions, physical difficulty notes.

## 3. Editorial guide (.docx)

One per source family per city (the Japan build produced "CNT Guide - Tokyo" and so on). Structure:

1. **Summary line with counts by category**, plus an outline of what the source family covers well
   and where it is thin. The traveler asked for an outline/summary at the top.
2. **Index table by category**, place name hyperlinked to Maps, with Type / Neighborhood / Hours /
   RES columns.
3. **The picks**, grouped by category, each with the editorial note and the Maps link.
4. **Consensus section**: places that appeared in three or more independent sources.

Filter rules for editorial harvests, stated by the traveler: **no hotels, no Airbnbs, no packing lists, no
out-of-season content** (skip ski resorts and Christmas markets for a July trip). Prune during
extraction, not after.

## 4. Google Maps CSVs

### The mechanics (verified on the Japan build)

- Import target is **Google My Maps** (`mymaps.google.com`), not Google Maps Saved lists. Saved lists
  have no bulk import.
- One CSV becomes one **layer**. A map holds **10 layers**, a layer holds **2,000 features**.
- Different icons within a layer come from **Style by data column, Categorize**, pointing at the
  `Subcategory` column. Practical cap is about **30 distinct values per layer**, so keep subcategory
  vocabularies tight.
- Geocoding runs off one column. Use `Location` (the `maps_query` field). Set the name column to
  `Name` and the description column to `Note`.
- Geocoding is imperfect for small venues. Anything ambiguous should carry a more specific
  `maps_query` (add the neighborhood and country) or a `verify-open` flag.

### Header (fixed)

```
Name,Location,Category,Subcategory,Neighborhood,Hours,Res,Price,Note,Source,MapsURL
```

`MapsURL` is a convenience column, not used by the importer:
`https://www.google.com/maps/search/?api=1&query=<urlencoded maps_query>`

### The `Note` column format (the traveler's explicit ask)

The note is what shows in the Maps pin popup, so it carries the compact hours and the reservation
flag inline. Assemble it as:

```
<Subcategory> | <hours compact> | <RES tag + how> | <note text> | <price>
```

Worked examples:

```
Omakase | Tu-Sa 18:00-22:00, closed Su M | RES 1-2mo via Pocket Concierge | Edomae counter, warm aggressively vinegared shari, no ordering | ¥30,000-35,000 / $200-235
Temple | daily 6:00-18:00 | no booking | Founded 778, 1633 halls built without nails, UNESCO | ¥500 / $3.30
Knife Shop | W-M 10:00-18:00, closed Tu | no booking | Hand-forged Sakai blades, free sharpening lesson, ships worldwide | ¥15,000-60,000 / $100-400
Museum | Tu-Su 10:00-17:00 (last entry 16:30), CLOSED Mondays | RES same-day timed entry | ... | ¥1,200 / $8
```

Use `CLOSED <days>` in caps when the closed day is the thing most likely to wreck a plan. Keep the
whole note under about 350 characters so the popup stays readable.

### File sets to produce

| Folder | Files | Purpose |
|---|---|---|
| `MAPS - Master/` | one per city plus one for day trips | The set to actually import. All categories, all sources, deduped. |
| `MAPS - By Category/` | city x category | For maximum icon control, when a city has enough places that one layer is unwieldy. |
| `MAPS - Editorial/` | one per source per city, plus one combined mass-upload | Keeps editorial provenance separate. |

Encoding: **`utf-8-sig`** (BOM) on every CSV so Excel opens it without mangling accents and local
script. Learned on the Japan build.

Ship a `README-import-guide.txt` in each folder: the import steps, the style-by-data instructions,
the layer limits, and the geocoding accuracy caveat.

## 5. Reservation tracker

Columns: Deadline / What / City / How to book / Cost / Lead time / Backup if it fails / Booked? /
Confirmation. Sorted by deadline ascending. This is the single most actionable artifact; it should be
extractable straight out of the record set by filtering `res` to anything stricter than `RES:none`.

---

## Formatting invariants (all documents)

| Rule | Value |
|---|---|
| Margins | 0.5 inch, all four sides, every section |
| Body font | Calibri 10.5 |
| Heading colour | Navy `#041E42` for H1 and H2, steel `#2A4A6A` for H3 |
| Link colour | `#0563C1`, underlined, real `w:hyperlink` relationships |
| Tables | `Table Grid` style, header row shaded navy with white bold text, body rows banded by category |
| Flags | Red text, bracketed, e.g. `[UNESCO]`, `[VERIFY OPEN]` |
| Prices | Local currency first, USD second, per person, state inclusions |
| Em dashes | Never. Commas, colons, periods, parentheses. |
| Emojis | Not in prose. Permitted only inside the compact-hours notation if a closed marker is used. |
| Library | `python-docx` only. Never raw zipfile manipulation. |
| Pre-flight | Document re-opens via `Document(path)`; every hyperlink relationship resolves; no table has an empty row. |
