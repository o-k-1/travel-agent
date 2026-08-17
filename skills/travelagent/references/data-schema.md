# Canonical Place Record Schema

Everything the skill produces flows from one record type. Research subagents emit it, the Word
builder reads it, the Google Maps CSV writer reads it. One schema, no translation layers.

## Why pipe-delimited for agent output

Subagents return **pipe-delimited (` || `) lines**, not CSV and not JSON. Learned on the Japan build:

- CSV from an LLM breaks on embedded commas and unbalanced quotes, silently shifting columns.
- JSON from an LLM breaks on trailing commas, smart quotes, and unescaped newlines, and one bad
  record kills the whole parse.
- ` || ` with a strict field count is self-validating: count the fields, drop malformed lines, log
  them. A single bad line costs one place, not the whole batch.

Normalize HTML entities before writing (`&amp;` to "and", `&#39;` to an apostrophe). A stray `|`
inside a field name must be replaced with a slash.

## Field list

Field order is fixed. 18 fields.

| # | Field | Required | Values / format | Notes |
|---|---|---|---|---|
| 1 | `city` | yes | `Tokyo`, `Kyoto`, `DayTrip`, `Other` | The Maps layer and doc grouping key. Use `DayTrip` for anything outside the base cities, `Other` for national/regional entries. |
| 2 | `category` | yes | one of the 8 below | Drives doc section and CSV file split. |
| 3 | `subcategory` | yes | free text, title case | **This is the Google Maps icon key.** Keep the distinct count per layer under 30. |
| 4 | `name` | yes | display name, Latin script | No parentheticals; put local script in `local_name`. |
| 5 | `local_name` | no | local script | For showing a taxi driver or a shop sign. Empty string if none. |
| 6 | `maps_query` | yes | `<name> <neighborhood> <city> <country>` | The geocoding string. Never a URL. Strip `&`, parentheses, and commas. |
| 7 | `neighborhood` | yes | short text | The clustering key for proximity planning. |
| 8 | `cluster` | yes | short text | The walking-order group used in the detailed writeup. Often equals `neighborhood`, sometimes wider ("East Kyoto: Higashiyama"). |
| 9 | `hours` | yes* | compact notation, see `hours-and-closures.md` | `*` Required for anything with hours. Use `24h` or `always open` for parks and streets, `unknown, verify` if genuinely unknown. Never invent hours. |
| 10 | `closed` | no | closure notes | Weekly closures already live in `hours`. This field is for date-specific and seasonal closures: `closed Aug 13-16 (Obon)`, `closed for renovation until 2027`, `closed 3rd Wed`. |
| 11 | `res` | yes | one of the RES tags below | Never blank. `RES:none` is a real answer. |
| 12 | `res_how` | no | platform, URL, or method | `OMAKASE (omakase.in)`, `hotel concierge only`, `official site timed entry`, `queue from 07:00`, `phone, Japanese only`. |
| 13 | `price` | no | `<local> / <USD>` | `¥25,000-30,000 / $165-200 pp, no drinks`. Free sites: `free`. Ticketed sites: include the ticket price. |
| 14 | `tier` | yes | `anchor` / `strong` / `alternate` | See tiering rules below. |
| 15 | `note` | yes | 1 to 3 sentences | What it is known for, what to order or look at, why it matters. This is what lands in the Maps note field. |
| 16 | `why` | no | 60 to 180 words | The detailed-writeup body. Historical argument, architectural read, or the dish's story. Empty for minor entries. |
| 17 | `flags` | no | semicolon-separated | `UNESCO`; `verify-open`; `no-photography`; `cash-only`; `english-menu-no`; `stairs-heavy`; `books-out`; `tourist-trap-adjacent`; `seasonal`. |
| 18 | `source` | yes | provenance | `CNT`, `NYT36`, `Eater`, `Michelin`, `Research`, `Tabelog`, or a combination joined with ` + `. Kept through merges so the master file shows consensus. |

### Categories (exactly these 8)

| Category | Contents | Maps layer |
|---|---|---|
| `Dining` | Restaurants, counters, stalls, bars, cafes, markets eaten at | one layer per city |
| `Clothes` | Menswear, boutiques, vintage clothing, tailors, textile shops | own layer, always separate from `Shopping` |
| `Shopping` | Knives, ceramics, craft goods, watches, cameras, books, records, department stores | own layer |
| `Sights-Sacred` | Temples, shrines, churches, mosques, cemeteries, gardens, parks | own layer |
| `Sights-Landmarks` | Castles, palaces, museums, towers, bridges, districts, viewpoints, memorials, architecture | own layer |
| `Activities` | Workshops, ceremonies, cycling routes, drives, hikes, onsen/baths, sport, classes, boat rides | own layer |
| `Nightlife` | Bars-as-destinations, live music, clubs, night districts | folded into `Dining` in Maps unless the count justifies its own layer |
| `Logistics` | Rental desks, luggage forwarding, IC card counters, IDP pickup, station lockers, post offices | own layer, small |

`Sights-Sacred` and `Sights-Landmarks` are split because the traveler asked for different icons by site type.
Inside each, `subcategory` (Temple / Shrine / Garden / Castle / Museum / Observation Deck) drives the
actual icon via Maps style-by-data.

### RES tags (field 11)

| Tag | Meaning |
|---|---|
| `RES:3-6mo` | Books out months ahead. Set a calendar reminder for the day the book opens. |
| `RES:1-2mo` | Book as soon as flights are ticketed. |
| `RES:2-4wk` | Book on trip confirmation. |
| `RES:1wk` | Book the week before. |
| `RES:2-3d` | Book a couple of days out. |
| `RES:same-day` | Same-day booking or timed entry released that morning. |
| `RES:walk-in` | No booking. Add queue behavior to `note` ("queue 30-60min at 11:30"). |
| `RES:lottery` | Ballot. Give the ballot window dates. |
| `RES:concierge` | Hotel concierge, local resident, or introduction required. |
| `RES:none` | Nothing needed, just show up during hours. |

Every record carries one. A blank `res` is a bug, not an omission.

### Tiering rules (field 14)

`tier` exists so the plan degrades gracefully when a reservation fails. the traveler's explicit ask: more
dining alternatives in case reservations are needed.

- `anchor` -- the intended booking or must-see. One per meal slot, one to three per day for sights.
- `strong` -- would be an anchor on another day; a first-choice substitute. Must be in the **same
  cluster** and the **same price band** as the anchor it backs up.
- `alternate` -- the walk-in-friendly or easy-booking fallback. At least one per anchor should be
  `RES:walk-in` or `RES:same-day` so there is a zero-risk option.

**Hard rule: every `anchor` dining record with `res` stricter than `RES:2-3d` must have at least two
non-anchor records in the same cluster and price band.** The build script checks this and fails loudly
if it does not hold. Same rule, softer, for sights: any anchor with `RES:lottery`, `RES:3-6mo`, or a
weather dependency needs one alternate.

## Example records

```
Tokyo || Dining || Omakase || Sushi Sho || 鮨さいとう || Sushi Sho Yotsuya Tokyo Japan || Yotsuya || Shinjuku-Yotsuya || Tu-Sa 18:00-22:00 (LO 20:30), closed Su M || closed Aug 12-18 || RES:1-2mo || Pocket Concierge or hotel concierge; releases 1st of month || ¥30,000-35,000 / $200-235 pp, no drinks || anchor || Edomae counter run at a punishing pace; the shari is aggressively vinegared and warm, which is the whole point. Order nothing, say nothing, eat as it lands. || <60-180 word writeup> || books-out;cash-only || Research + Michelin
Tokyo || Dining || Omakase || Sushi Tokami || || Sushi Tokami Ginza Tokyo Japan || Ginza || Ginza || M-Sa 12:00-14:00, 17:00-22:00, closed Su || || RES:2-4wk || TableCheck || ¥22,000-28,000 / $145-185 pp || strong || Ginza counter known for aged tuna and a lighter hand with vinegar; the substitute if the Yotsuya booking fails. || || || Research
Tokyo || Dining || Standing Sushi || Uogashi Nihon-Ichi || || Uogashi Nihon-Ichi Shibuya Tokyo Japan || Shibuya || Shibuya || daily 11:00-23:00 || || RES:walk-in || none || ¥2,000-3,500 / $13-23 pp || alternate || Standing counter, per-piece ordering, no reservation and no ceremony. The zero-risk sushi option in the same evening slot. || || || Research
Kyoto || Sights-Sacred || Temple || Kiyomizu-dera || 清水寺 || Kiyomizu-dera Higashiyama Kyoto Japan || Higashiyama || East Kyoto: Higashiyama || daily 06:00-18:00 (summer to 18:30) || || RES:none || none || ¥500 / $3.30 || anchor || Founded 778, current halls 1633 under Tokugawa Iemitsu, built without a single nail. || <writeup> || UNESCO;stairs-heavy || Research + CNT
```

## Provenance and merging

When the same place appears from two sources, merge rather than duplicate:

1. Key on `(city, normalized_name)` where normalization strips non-alphanumerics and lowercases.
2. Keep the first record as the base. Union the `source` fields with ` + `, ordering `Research` first.
3. Replace `note` only if the incoming one is materially longer (more than 15 characters longer).
4. Union `flags`. Keep the more specific `hours` and the stricter `res`.
5. Never drop a `local_name`, `price`, or `res_how` that the base record lacks.

A place appearing in three or more independent sources is a **consensus pick**. Mark it in the doc.
That signal is worth more than any single listicle.
