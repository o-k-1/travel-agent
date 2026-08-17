# Hours, Closures, and Seasonal Risk Reference

Region-agnostic reference for trip planning: how to notate operating hours compactly, what typically closes on which day by venue type and region, which public holidays shut down a city or a country, which categories are seasonal, and where to verify hours before committing a day plan to it. Japan appears only as one example among many; every rule here is meant to generalize to any country.

Unverified or approximate items are marked "(unverified)". Do not treat any specific hour, date, or closure claim in this file as current without checking the venue's own source before a trip; patterns are durable, individual hours are not.

---

## 1. Compact hours notation standard

### 1.1 Core grammar

```
<days> <hours>[, <hours2>]; <modifier>[, <modifier2>...]
```

- **Days**: a day range or list, using the abbreviations in 1.2.
- **Hours**: a time range. Use 24h by default (see 1.3). A comma inside the same day range separates split shifts (lunch/dinner).
- **Semicolon**: separates independent day-blocks or attaches a modifier (closure note, seasonal note, irregular-hours flag).
- **CLOSED**: written in caps when a day range is fully shut, so it scans instantly in a table cell.

Base example from the style this notation is built on:

```
M-R 9-4; CLOSED F-Su
```

This reads: Monday through Thursday, 9am-4pm; closed Friday through Sunday. That exact string has one flaw worth fixing before adopting it as a standard: **R for Thursday is ambiguous** (see 1.2). The recommended rewrite is:

```
M-Th 9-4; CLOSED F-Su
```

### 1.2 Day abbreviations

| Day | Recommended abbreviation | Notes |
|---|---|---|
| Monday | M | Unambiguous |
| Tuesday | Tu | Never "T" alone, collides with Thursday |
| Wednesday | W | Unambiguous |
| Thursday | Th | **Not "R".** R is a convention from some US library/scheduling systems (M T W R F) but is not widely known, gets misread as a typo, and does not survive copy-paste into a Google Maps note field where a reader has zero context. Always spell "Th". |
| Friday | F | Unambiguous |
| Saturday | Sa | Never "S" alone, collides with Sunday |
| Sunday | Su | Never "S" alone, collides with Saturday |

Ranges: `M-Th` (Monday through Thursday, inclusive). Lists: `M,W,F` (Monday, Wednesday, and Friday only). Combined: `M-W,F-Su` (closed Thursday only).

### 1.3 24h vs 12h

- **Default to 24h clock** (`9-16` or `09:00-16:00`) for the compact notation. It is shorter, has no AM/PM ambiguity, and sorts correctly in a spreadsheet.
- Use bare hour numbers without leading zero or colon when minutes are `:00` and the context is unambiguous: `9-4` for 9am-4pm is acceptable **only** in a same-day range where readers will infer AM-open/PM-close from context (this is the one place 12h-style shorthand survives, because `9-4` in 24h would mean 9am to 4pm, not 9am to 4am; the notation leans on convention, not brackets).
- For anything spanning noon or using half-hours, use full 24h with colons: `11:30-14:00`, `17:30-21:00`.
- Never mix bare-number shorthand with 24h afternoon numbers in the same field (`9-16` is fine, `9-4pm` is not; pick one).
- For a Word-doc table with more room, spell out `9:00 AM - 4:00 PM` if the audience is non-technical; for a CSV note field, always use the compact 24h form because commas and AM/PM markers can break CSV parsing or get truncated in a Maps popup.

### 1.4 Split service (lunch and dinner shifts)

Comma-separate two ranges within one day-block:

```
Tu-Su 11:30-14:00, 17:30-21:00; CLOSED M
```

If lunch and dinner have different day patterns (e.g., dinner-only on a slower night), split into separate blocks:

```
Tu-Sa 11:30-14:00, 18:00-22:00; F-Sa +23:00 late seat; CLOSED M,Su
```

### 1.5 Last order (LO) vs close time

Kitchens routinely stop taking orders before the room closes. If both are known, express both; if only LO is known, lead with it since it is the operative constraint for a diner walking up late.

```
18:00-23:00 (LO 22:00)
```

Reads as: doors open 18:00, room closes 23:00, kitchen stops taking orders at 22:00. If a bar keeps serving drinks after LO, that is implied by the close time; call it out explicitly only if it diverges further: `LO food 21:30, bar to 24:00`.

### 1.6 Seasonal variance

Append a season tag in brackets when hours shift with season. Use short season words, not month ranges, when the venue's own seasonal boundary is fuzzy or shifts year to year; use explicit months when it is fixed.

```
[summer] 9-19; [winter] 10-16
Apr-Oct 9-18; Nov-Mar 10-16, CLOSED W
```

### 1.7 "Closed 3rd Wednesday" (and other periodic closures)

Ordinal-day closures are common for maintenance days at museums, libraries, and some government offices. Notate as an ordinal + day:

```
M-Su 9-17; CLOSED 3rd-W (monthly maintenance)
```

Other ordinal patterns to support: `1st-M`, `last-Su`, `2nd+4th-Tu` (biweekly on the pattern). Always add a 2-4 word parenthetical reason if known; it helps a traveler decide whether to double-check that week specifically.

### 1.8 Irregular closures

Some venues (chef-driven restaurants, artisan workshops, small galleries) do not run a fixed schedule and closures are announced ad hoc. Do not invent a fake regular schedule for these. Use a flat flag:

```
irregular, check IG
irregular, call ahead
irregular, see [official site]
```

This is a legitimate and common notation state, not a placeholder to be avoided; it correctly signals to the planner "do not build a tight itinerary around this stop without a same-week check."

### 1.9 Last entry before close (museums, gardens, attractions with a visit duration)

Ticketed sites frequently stop admitting visitors before the stated close time, because they need visitors to have time to actually see the thing. Notate as an offset from close, which stays correct even if the site's overall hours later change:

```
9-18 (last entry -60m)
9-18 (last entry 17:00)
```

Prefer the offset form (`-60m`) over an absolute time when documenting a pattern that recurs at many venues in the same country (offsets are more often stable than absolute last-entry clocks, which shift with the close time).

### 1.10 24-hour venues

```
24h
Su-Th 24h; F-Sa CLOSED 02:00-06:00
```

Some markets, konbini-style convenience formats, and transit-linked venues run continuously; others run 24h on weekdays but close briefly overnight for cleaning on weekends. State the exception explicitly rather than writing "24h" for a venue that has one weekly gap.

### 1.11 "Closed the day after a public holiday"

This is a real, recurring pattern, not just a Japan quirk (Japan's museum substitute-closure rule is the most codified version; see Section 2 and Section 3). The general notation:

```
M-Su 9-17, CLOSED M; +CLOSED day-after-holiday-if-Mon-is-holiday
```

Shorthand for the same idea, more compact for a CSV field:

```
CLOSED M (+Tu if M is holiday)
```

The underlying logic to encode, regardless of country: when a venue's normal closure day coincides with a public holiday and the venue stays open on the holiday itself (to capture holiday footfall), the closure shifts to the next non-holiday weekday. Always verify this against that specific country's / venue's actual practice; some venues just close on the holiday AND on their normal day, stacking two closures instead of shifting one.

### 1.12 Quick-reference marker card

For a Word-doc appendix or a shared team reference, the markers below are the complete vocabulary this notation needs. Keep this card next to any table that uses the notation so a reader unfamiliar with it can decode a cell in seconds.

| Marker | Meaning | Example |
|---|---|---|
| `M Tu W Th F Sa Su` | Day abbreviations | `Tu-Th` |
| `-` between days | Inclusive range | `M-F` |
| `,` between days | Discrete list | `M,W,F` |
| `,` between hour blocks | Split shift (same day range) | `11:30-14:00, 17:30-21:00` |
| `CLOSED` | Fully shut that day/range | `CLOSED Su` |
| `(LO hh:mm)` | Last order time, distinct from close | `18-23 (LO 22:00)` |
| `(last entry -Xm)` or `(last entry hh:mm)` | Last admission before close | `9-18 (last entry -60m)` |
| `[season]` or explicit months | Seasonal hours block | `[summer] 9-19; [winter] 10-16` |
| `Nth-Day` | Ordinal periodic closure | `CLOSED 3rd-W` |
| `irregular, check X` | No fixed schedule, verify via named channel | `irregular, check IG` |
| `24h` | Continuous operation | `24h` |
| `(+CLOSED day-after-holiday...)` | Holiday-shift rule | `CLOSED M (+Tu if M is holiday)` |
| `by appointment only` | No walk-in service | `by appointment only; CLOSED M` |

### 1.13 CSV field vs. Word-table rendering of the same venue

The same underlying schedule should compress differently depending on where it lands. A Google Maps CSV note field is character-constrained and machine-adjacent (other tools may parse it); a Word table cell has more visual room and a human reader who benefits from a slightly looser, more legible form.

| Context | Rendering | Why |
|---|---|---|
| Google Maps CSV note field | `Tu-Su 11:30-14:00,17:30-21:00;CLOSED M;LO 21:30` | No internal spaces around commas/semicolons where avoidable, since some CSV/URL contexts trim or mis-split on stray whitespace; keep it on one line |
| Word-doc table cell | `Tu-Su: 11:30-14:00, 17:30-21:00 (LO 21:30)` / `Closed Monday` on its own line below | Spell out "Closed Monday" instead of `CLOSED M` when the audience is a client or non-technical reader; keep the compact hours but drop the terse day-code once space allows a real word |
| Internal planning sheet (traveler-facing) | Full compact notation exactly as documented in 1.1-1.11 | Fastest to scan across a dense multi-row itinerary; the traveler using this file has already learned the notation |

### 1.14 Worked examples across venue types

| # | Venue type | Compact notation | Reading |
|---|---|---|---|
| 1 | Neighborhood museum | `CLOSED M; 9-17 (last entry -30m)` | Closed Monday; open 9-5 other days, last entry 4:30 |
| 2 | Major national museum (Tuesday-closure country) | `CLOSED Tu; 10-18 (last entry -45m)` | Closed Tuesday instead of the global-default Monday |
| 3 | Fine-dining restaurant, split service | `Tu-Sa 12:00-14:00, 19:00-22:00 (LO 21:00); CLOSED Su-M` | Lunch and dinner shifts, kitchen closes 1hr before room |
| 4 | Izakaya / late-night bar | `18:00-01:00 (LO food 24:00); CLOSED irregular Su` | Late kitchen cutoff before bar close; Sunday closure not fixed |
| 5 | Ramen counter, no reservations | `11-15, 18-21; CLOSED W; sells out ~30min before close` | Split shifts; practical early-closure risk beyond stated hours |
| 6 | Wholesale produce/fish market | `M-Sa 5-10 (auction 5-7, public floor 8-10); CLOSED Su + holidays` | Auction-only early window, public-facing hours later |
| 7 | Government permit office | `M-F 9-16:30 (LO new applications 15:30); CLOSED Sa-Su + public holidays` | Cutoff for starting new business before close |
| 8 | Consulate visa window | `M-Th 9-12 (submissions only); pickup Tu,Th 14-16; CLOSED F` | Split function by time-of-day, not just day |
| 9 | Mosque, non-prayer visiting hours | `9-12, 14-16:30; CLOSED during 5 daily prayer windows (~20-30min each) + all F midday (Jumu'ah)` | Recurring intraday closures unrelated to the open/close envelope |
| 10 | Cathedral / parish church | `9-18; CLOSED to tourists Su 8-12 (services); reduced access during Mass' | Sunday morning is not a closure but a function change |
| 11 | Barbershop / tailor, appointment-only | `by appointment only; CLOSED M; walk-in Tu-F 10-13` | Booking norm stated up front, partial walk-in window |
| 12 | Ryokan / seasonal inn | `open Apr-Nov; CLOSED Dec-Mar (winter closure)` | Full seasonal shutdown, not a weekly pattern |
| 13 | Ski-season restaurant | `[winter] 8-16 (lift-dependent); CLOSED [summer]` | Operation tied to a separate operator's season, not calendar |
| 14 | 24h convenience format | `24h; restocking 4-5 (reduced counter service)` | Nominally 24h with a known service dip |
| 15 | Public bathhouse / onsen | `15-24 (LO 23:00); CLOSED 2nd-Tu (maintenance)` | Evening-leaning hours plus a periodic maintenance day |
| 16 | Beach club (seasonal + weather) | `[Jun-Sep] 10-19; CLOSED [Oct-May]; weather-dependent even in season` | Seasonal envelope plus a same-day risk flag |
| 17 | Small gallery, artist-run | `irregular, check IG; usually Th-Su 12-18` | Irregular flag with a best-guess fallback pattern |
| 18 | Day-after-holiday shift (any country) | `CLOSED M (+Tu if M is public holiday)` | Encodes the shift rule directly in the notation |

---

## 2. Standard weekly closure patterns by venue type and region

### 2.1 Museums

| Pattern | Where it holds | Notes |
|---|---|---|
| Closed Monday | Global default: most of Western Europe, the Americas, much of Asia | Treat Monday-closed as the base assumption unless told otherwise |
| Closed Tuesday | Louvre and several other major Paris museums (Musée de l'Orangerie, Centre Pompidou, Musée Guimet), some Madrid museums (Reina Sofía), some Italian museums (Naples archaeological museum, Venice's Peggy Guggenheim and Ca' Rezzonico), some US institutions (unverified for current-year specifics; the pattern of splitting closure days across a city's flagship museums so at least one major museum is open on any given weekday is deliberate in Paris) | Never assume all museums in a city share the same closure day; check each flagship individually |
| Closed Sunday | Vatican Museums (with the exception of the last Sunday of each month, when entry is free); (unverified) some smaller regional/municipal museums elsewhere | Distinct from the Monday/Tuesday pattern; driven by religious observance in the Vatican's case |
| Open 7 days, no weekly closure | Some flagship national museums with heavy tourist footfall (e.g., British Museum, National Gallery London, Prado Madrid) (unverified for exact current-year policy) | Increasingly common for the very top tier of tourist-driven institutions; still verify annual maintenance closures |
| Closed on national holidays even if not the normal closure day | Widespread but inconsistent; some sites do the opposite (stay open on holidays, close the following day instead) | See Section 1.11 and Japan's substitute-closure rule below |

Country-specific closure-day tendencies worth flagging to a traveler (verify per venue, this is a starting prior, not a rule):

| Country/region | Typical museum closure day |
|---|---|
| France | Split: Louvre/Pompidou/Orangerie Tuesday; Orsay, Rodin, Versailles Monday |
| Italy | Mixed Monday/Tuesday depending on city and institution; many municipal museums Monday |
| Spain | Mixed; several major Madrid museums Monday, Reina Sofía Tuesday |
| Vatican City | Sunday (with last-Sunday-of-month exception) |
| Japan | Monday is the default for national/prefectural museums, with the day-after-holiday shift rule (Section 3) |
| United States | Mostly no fixed weekly closure at major institutions; smaller/regional museums often Monday |
| Germany | Monday common for state museums; some exceptions |

### 2.1a "Which countries close Tuesday instead of Monday" (quick answer)

Since this is one of the most common planner questions, here is the direct answer distilled from 2.1: no country closes its museums on Tuesday as a national default. Monday-closure is the near-universal default worldwide. Tuesday-closure is an institution-by-institution exception layered on top of that default, concentrated in:

- France: the Louvre and several other flagship Paris museums close Tuesday specifically so the city always has at least one major museum open on a Monday (when most others are shut).
- Spain: a subset of major Madrid museums (Reina Sofía) follow the same Tuesday pattern; others (Prado) run 7 days with no weekly closure.
- Italy: mixed at the individual-institution level, notably several Venice and Naples museums, rather than a national rule.

Practical guidance: never assume "Tuesday is safe because Monday is the closure day" in any of these three countries without checking the specific institution. The exception exists precisely to spread closures across the week within a single city, which means a city's museums as a group are rarely all closed on the same day, but an individual museum's day is not predictable from the country alone.

### 2.2 Fine dining

| Pattern | Where it holds |
|---|---|
| Sunday and Monday "dark days" | Common convention across Western fine dining (US, UK, much of Western Europe): staff need consecutive days off, Sunday and Monday are traditionally the lowest-cover nights |
| Sunday-only dark day | Common in cities with strong weekend brunch/lunch culture; Monday stays open |
| August closure (2-4 weeks) | Widespread in France, Italy, and parts of continental Europe; many independent restaurants close for annual staff holiday, historically tied to the industrial "August shutdown" |
| Closed Sunday and public holidays | Common pattern for independent Japanese restaurants (izakaya, sushi-ya, soba shops); many close both the weekly day and stack a holiday closure rather than opening through it |
| Riposo / afternoon closure | Spain and Italy: many traditional restaurants and shops close mid-afternoon (roughly 14:00-17:00 or later) between lunch and dinner service, especially outside major tourist centers |
| Closed Monday specifically | Common in Italy for restaurants (echoing the barber/artisan Monday-closure norm, Section 2.6) and in France for some bistros |

### 2.3 Markets

| Pattern | Where it holds |
|---|---|
| Closed Sunday (retail floor) | Most wholesale produce, fish, and flower markets run a public-facing retail component that shuts Sunday even if some functions continue |
| Closed Monday | Some fish markets close Monday specifically because Sunday is the day boats don't go out, leaving nothing to auction Monday morning |
| Auction-only early morning window | Wholesale fish and flower markets frequently restrict the actual auction to a narrow pre-dawn window (often not open to the public at all, or viewing-only) with a separate, later public retail window |
| Closed public holidays, often for multiple days | Markets tend to track national holiday clusters closely (see Section 3) since suppliers and buyers both shut down |

### 2.4 Shops

| Regulatory pattern | Country/region | Notes |
|---|---|---|
| Strong Sunday trading restriction (near-total ban with limited "shopping Sundays") | Poland | Since 2020; specific permitted Sundays are set annually and are few (roughly 7-8/year), often tied to pre-Easter and pre-Christmas periods (unverified for exact annual list; changes year to year) |
| Full Sunday closure as constitutional norm ("Sonntagsruhe" / day-of-rest laws) | Germany | Exemptions: train station/airport shops, gas stations, pharmacies; individual states permit a limited number of designated "shopping Sundays" per year tied to local events |
| Strict Sunday closure | Austria | Shops generally closed Saturday evening through Monday morning; exemptions at major rail hubs, airports, and specific tourist zones |
| Heavily regulated Sunday trading | Norway | Small grocery formats under a defined size cap, gas stations, pharmacies, and shops in designated tourist destinations may open; general retail stays closed |
| Decentralized, largely open Sundays in cities | Netherlands | Municipalities decide; major cities (Amsterdam, Rotterdam, Utrecht) generally allow Sunday shopping, smaller towns may not |
| Midday closure / siesta | Spain, parts of Italy, parts of Latin America | Small and traditional retail (not chains/malls) closes roughly early-to-mid afternoon and reopens early evening; increasingly eroded in tourist centers and large cities |
| Sabbath closure (Friday sunset to Saturday nightfall) | Israel, and Jewish-owned businesses in some diaspora neighborhoods | Most shops, public transit in many areas, and many restaurants close for Shabbat; some hotels and Arab-owned or secular-run businesses stay open |
| Friday midday closure / reduced hours for Jumu'ah prayer | Muslim-majority countries generally | Many shops and offices close or pause for a window around Friday midday prayers; duration varies by country and how strictly observed locally |
| Ramadan hours shift | Muslim-majority countries generally | Many shops/offices shift to shorter daytime hours and longer evening hours; some businesses close entirely in the afternoon and reopen after iftar; restaurants serving daytime meals may be closed or discreet during fasting hours; see Section 3 for date ranges |

### 2.5 Religious sites

| Pattern | Notes |
|---|---|
| Closed to visitors during active services | Churches, mosques, synagogues, temples, and shrines routinely restrict or halt tourist access during services/prayers; this is a recurring intraday closure, not a weekly day-off |
| Mosques: closed to non-worshippers during the five daily prayer windows | Each window is short (roughly 20-30 minutes) but recurs five times a day; Friday midday (Jumu'ah) closure to tourists is typically longer |
| Churches: reduced or no tourist access Sunday morning | Especially cathedrals and active parish churches; Sunday Mass schedules can block off several hours |
| Temples/shrines: closed or restricted during festivals and rites | Timing is often lunar-calendar-based and site-specific; check the specific site's calendar near the travel date |
| Some sites charge/restrict entry outside of specific open windows even when not mid-service | Common at major pilgrimage sites; treat as a distinct closure category from both weekly and holiday closures |

### 2.6 Government / office-hour sites

| Pattern | Notes |
|---|---|
| Business-hours-only, Monday-Friday | Consulates, permit offices, and most government counters run standard weekday office hours (commonly ending mid-afternoon for public-facing service even if staff work later) |
| Split function by time of day | Many consulates take new applications only in the morning and do pickups/collections only in the afternoon, or vice versa; verify per office |
| Closed on both home-country and host-country public holidays | Consulates typically observe both the host nation's holidays and their own national holidays, roughly doubling the closure-risk calendar compared to a local business |
| Closed to unscheduled visitors, appointment-only | Increasingly the norm for visa/passport services; walk-in service is being phased out at many posts |

### 2.7 Barbers, tailors, and artisan workshops

| Pattern | Where it holds |
|---|---|
| Monday closure | Widespread in Italy for barbers, hairdressers, and many artisan trades; echoes the "shops that serve the public rest on the day after the weekend rush" logic seen elsewhere in Southern Europe |
| Appointment-only as the default, not the exception | Common globally for tailors, cobblers, and specialty artisan workshops (as opposed to walk-in barbershops); a walk-in visit risks a wasted trip |
| Extended midday closure | Same riposo/siesta logic as retail in Spain/Italy applies to independent artisan shops |
| Seasonal reduction | Some artisan workshops (particularly in tourist-dependent towns) reduce days or close entirely in the off season |

---

## 3. Public holiday closure risk by region

Effect key: **Everything closed** = most businesses, transit-adjacent services may still run but tourism infrastructure and offices shut. **Everything booked out** = venues stay open but capacity (trains, hotels, restaurants, attractions) sells out well in advance and walk-up access becomes unreliable. **Transport chaos** = normal transport capacity is overwhelmed by domestic travel demand, not a closure per se.

| Region | Holiday cluster | 2026 dates (verified where noted) | Effect |
|---|---|---|---|
| Japan | Golden Week | Apr 29 - May 6, 2026 (verified) | Everything booked out; transport chaos; many small businesses close for part/all of the window |
| Japan | Obon | Aug 13-16, 2026 in most of Japan (verified; Tokyo/northern Japan sometimes observes mid-July instead, Okinawa later, per lunar variant) (unverified regional-variant specifics) | Transport chaos around the edges of the window; many family-run businesses close; offices often take extended leave |
| Japan | New Year (Shogatsu) | Approx. Dec 29 - Jan 3 each year (pattern, not date-specific) | Everything closed: most museums, restaurants, and shops shut for the full window regardless of weekday; this is the most total shutdown period in Japan's calendar |
| Japan | Silver Week | Sept 19-23, 2026, a rare full 5-day Silver Week this year (verified; next full 5-day recurrence not until 2032 per source) | Everything booked out; transport chaos |
| Japan | Day-after-Monday-holiday museum rule | Recurring rule, not a single date: when a national holiday falls on a museum's normal closure day (commonly Monday) and the museum opens on the holiday to capture footfall, closure shifts to the next non-holiday weekday (commonly Tuesday) (verified pattern, specific 2026 dates unverified in detail beyond the general rule) | Localized closure risk: this is a common cause of "why is this specific museum closed today" surprises when a Monday holiday is in the itinerary |
| China | Chinese New Year (Spring Festival) | Feb 17, 2026 (Year of the Horse); official holiday period Feb 15-23, 2026, a 9-day break (verified) | Everything closed and booked out simultaneously: this is the single largest closure/travel event in China's calendar (Chunyun migration); factories, government offices, and most small businesses close for the full period |
| China | Golden Week (National Day) | Oct 1-7, 2026 (verified) | Everything booked out; transport chaos; major tourist sites at extreme capacity |
| Europe | Easter / Semana Santa | Easter Sunday Apr 5, 2026; Holy Week runs Mar 29 - Apr 5, 2026 (verified) | Everything booked out in Spain (especially Seville, Málaga) and Mexico for Semana Santa processions; many businesses closed Good Friday and Easter Monday depending on country |
| Europe | Ferragosto | Aug 15 (fixed date, Assumption of Mary) | Everything closed across Italy, and to a lesser extent Spain/France/Austria; often the peak of a broader 2-4 week August shutdown of small businesses |
| Europe | French August closures | Roughly all of August, concentrated around the 15th | Everything closed for many independent restaurants, shops, and artisan workshops in France (and similarly in Italy/Spain); this is a structural annual-leave pattern, not a single-day holiday |
| Europe | All Saints' Day | Nov 1 (fixed date) | Everything closed in Catholic-majority countries (France, Spain, Italy, Poland, etc.); often a long-weekend travel bump |
| Europe | Christmas / Boxing Day cluster | Dec 24-26, extending informally to Jan 1-2 in many countries | Everything closed; multi-day shutdown common across most of Europe |
| Europe | Spanish/Italian local fiestas | Dates vary by town (patron saint days, local ferias) | Everything closed in that specific town only; high localized risk that is easy to miss because it doesn't appear on a national holiday calendar |
| Europe | Carnival (Venice, Rio-linked Mardi Gras timing, Tenerife) | Feb 2026 window, culminating Fat Tuesday Feb 17, 2026 (verified for Venice Jan 31-Feb 17, Tenerife Feb 11-22) | Everything booked out in host cities; some closures on the core parade days |
| Middle East | Ramadan | Approx. Feb 18 - Mar 19, 2026 (verified, moon-sighting dependent, +/-1 day); approx. Feb 8 - Mar 8, 2027 (unverified estimate, moon-sighting dependent) | Shifted hours rather than full closure: many businesses run shorter daytime hours and extended evening hours; some restaurants closed or discreet during fasting hours in daytime; Eid al-Fitr that follows causes a short everything-closed/booked-out spike |
| Middle East | Eid al-Fitr | Approx. Mar 20, 2026 (verified estimate); typically 1-3 day national holiday, longer in practice | Everything closed for the holiday itself, often extending 3+ days informally |
| Middle East | Eid al-Adha | Approx. May 27-30, 2026 (verified estimate) | Everything closed for several days; major domestic and regional travel bump |
| Latin America | Semana Santa | Mar 29 - Apr 5, 2026 (shared with European Easter dating); many countries extend to a two-week "Semana Santa + Semana de Pascua" period (unverified for exact country-by-country extension) | Everything booked out at coastal/resort destinations; many offices and some businesses closed the Thursday-Friday-Saturday core |
| Latin America | Carnival (Rio and broader Brazil) | Feb 13-17, 2026, with the elite Samba School parades Feb 14-15 and Champions Parade Feb 21 (verified) | Everything closed/booked out in host cities; this is the peak closure/travel-chaos event of the Brazilian calendar |
| Latin America | Dia de Muertos | Nov 1-2 (fixed dates) | Everything closed in Mexico for the public holiday portion; high tourist demand at Oaxaca and Mexico City events specifically |
| India | Diwali | Main day (Lakshmi Puja) Nov 8, 2026; 5-day sequence roughly Nov 6-10, 2026 (verified) | Everything closed for the main days; transport chaos around the surrounding week as people travel home |
| India | Holi | Holika Dahan Mar 3, 2026; main day (Rangwali Holi) Mar 4, 2026 (verified) | Everything closed regionally (strength varies by state, strongest in North India); short-duration, high-intensity closure |
| United States | Thanksgiving | 4th Thursday of November (pattern; falls Nov 26, 2026) | Everything closed on the day itself; Wed-Sun around it sees transport chaos (heaviest US domestic travel weekend of the year) |
| United States | July 4th (Independence Day) | Jul 4 (fixed date) | Everything closed for the day; shorter-duration closure than Thanksgiving, some transport chaos if it falls near a weekend |
| Southeast Asia | Songkran (Thailand) | Apr 13-15, 2026, official national holiday, extending informally Apr 11-16 in Chiang Mai/Bangkok (verified) | Everything closed/booked out: many businesses close for the water-festival days, transport and hotels in festival cities sell out |
| Southeast Asia | Tet (Vietnam) | Lunar New Year Day Feb 17, 2026; official holiday period roughly Feb 14-22, 2026, 9 days (verified) | Everything closed: this is Vietnam's equivalent of Chinese New Year in scale; small businesses and many restaurants close for the full period, cities empty out as people travel to hometowns |
| Southeast Asia | Nyepi (Bali, Indonesia) | Mar 19, 2026, 24-hour total shutdown from 6am Mar 19 to 6am Mar 20 (verified) | Everything closed, absolutely: airport fully closed to all flights, all roads/ports closed, no lights or noise permitted, tourists confined to their hotel grounds by law; this is the most total single-day shutdown in this entire reference, more absolute than any Western holiday closure |

---

## 4. Seasonal open/closed windows

| Category | Typical seasonal window | Rule of thumb / how to check |
|---|---|---|
| Mountain roads and high passes | Northern Hemisphere: typically late spring to early autumn (roughly May/June - Oct, highly elevation-dependent); Southern Hemisphere: invert to roughly Nov - Apr | Higher elevation = shorter season and later opening; always check the specific pass's current-year opening announcement, snowfall varies year to year by weeks |
| High-altitude hiking trails | Mirrors mountain-pass logic; many close for snow, avalanche risk, or hut-service season even when the trailhead road is open | Check the trail-managing authority or hut/refuge booking calendar, not just the general weather |
| Ferry seasons | Many seasonal ferry routes (island-hopping, fjord, lake routes) run reduced or zero schedules outside a summer window | Off-season schedules can drop to a fraction of frequency or stop entirely; verify per specific route, not per country |
| Ski vs. summer operation | Alpine resorts commonly flip business model between ski season (winter) and hiking/biking season (summer), with a shoulder-season full closure in between (spring and/or autumn) | The shoulder gap (commonly several weeks in Apr-May and again in Oct-Nov) is a common trap: neither the ski lifts nor summer trails are running |
| Beach clubs | Seasonal in temperate/Mediterranean climates (roughly May/Jun - Sept); year-round in tropical climates but still weather-dependent | In-season does not guarantee open on a given day; wind/tide/red-flag conditions can close a beach club same-day |
| Outdoor cinemas | Warm-season only in temperate climates; some tropical/dry-season locations run seasonally opposite (dry season rather than heat) | Follow the local dry/rain-season pattern rather than assuming a Northern Hemisphere summer default |
| Seasonal-only restaurants | Common at ski resorts, beach destinations, and harvest-linked venues (truffle season, mushroom season, specific fish runs) | If the draw is a specific seasonal ingredient, the venue's open window tracks that ingredient's season, not the calendar year uniformly |
| Ryokan / hotel annual maintenance closures | Many traditional inns and some hotels close for 1-4 weeks annually for maintenance, often in a low-demand shoulder month | Always confirmed at booking time; these closures are not always published far in advance |
| Museum annual renovation closures | Full-building or full-wing closures for months to years are common at major museums on a rotating basis | Check the specific museum's site for "currently closed galleries" before planning a visit around one specific work or wing |
| Monsoon season | South Asia (India, Bangladesh, Nepal): roughly Jun-Sept; Southeast Asia (varies by country, generally a wet season roughly May/Jun-Oct) | Affects outdoor activities, trekking, and some transport more than indoor venue hours; check region-specific monsoon calendars, timing varies significantly by country and coast |
| Typhoon season | East and Southeast Asia (Japan, Taiwan, Philippines, Vietnam, South China coast): roughly Jun-Nov, peak Aug-Oct (unverified for precise peak-month ranges, varies by sub-region) | Causes sudden transport and attraction closures rather than a predictable calendar closure; monitor forecasts in the days before travel during this window |
| Hurricane season | Atlantic basin (Caribbean, US Gulf/East Coast, Central America Atlantic side): Jun 1 - Nov 30 officially, peak Aug-Oct | Same dynamic as typhoon season: not a fixed closure, but a period of elevated risk for sudden cancellations |
| Wet/dry season for safaris and treks | Sub-Saharan Africa: varies sharply by region (East Africa often has two wet seasons; Southern Africa typically one, roughly Nov-Apr); Himalayan trekking: pre-monsoon (Mar-May) and post-monsoon (Sept-Nov) are the two main windows, monsoon season (Jun-Aug) is largely avoided | Do not apply one continent-wide rule; safari/trek operators publish specific optimal windows per region and these drive both animal-viewing quality and literal accessibility (flooded roads, closed trails) |

---

## 5. Where hours actually live and how to verify

Ranked roughly by authority, though the right order depends on venue type and how well-resourced the venue's own digital presence is.

| Rank | Source | Strength | Known failure mode |
|---|---|---|---|
| 1 | Official website / official social account of the venue | Beats Google Maps when it exists and is maintained; the venue is the ground truth | Small venues often have no site, or an outdated one; some sites don't post holiday-specific hours at all |
| 2 | Direct phone call | Highest confidence for a specific date, especially near a holiday or for irregular-hours venues | Language barrier; venue may not pick up during closed hours (which is itself informative) |
| 3 | Google Maps listing hours | Convenient, aggregates into itinerary tools, usually right for chains and well-resourced venues | **Frequently stale for small, owner-operated venues.** Hours get set once at listing creation and rarely updated; holiday-specific closures are almost never reflected, since owners update Maps even less often than their own site |
| 4 | Google Maps "Popular times" | Not an hours source, but useful for crowd/queue planning once you know it's open | Can be thin or absent for lower-traffic venues; reflects historical patterns, not this week's actual crowd (e.g., during a holiday cluster, historical data may not reflect current surge) |
| 5 | Instagram bio and recent Stories | Best real-time source for irregular closures at small restaurants, galleries, and artisan shops, since owners post same-day updates here before anywhere else | Stories expire after 24h and aren't searchable later; bio-link hours can be as stale as a website |
| 6 | Local-market review/booking platforms (e.g., Tabelog in Japan, or the equivalent trusted local platform in a given country) | Often more current and locally trusted than Google for food and service venues, because the local user base actively corrects listings | Not available or not authoritative outside its home market; requires knowing which platform is the trusted local one in a given country |
| 7 | International review/booking aggregators (TripAdvisor, Yelp, OpenTable-class booking pages) | Useful cross-check when a local platform doesn't exist or isn't in a language the planner reads; live booking-availability pages effectively confirm real open hours if a same-week slot exists | Reviews can be old; a listing showing as "temporarily closed" or with no recent activity is a signal to verify elsewhere before ruling a venue out entirely |
| 8 | Hotel concierge / front desk at the destination | Genuinely current local knowledge, including unwritten norms (siesta timing, which specific day a market is quietest, whether a holiday closure is actually being observed this year) that no listing captures | Only available once already at the destination; not useful for pre-trip planning, but valuable for the 48-hour re-check once on the ground |

Practical rule: for a chain, a major museum, or a government office, Google Maps is usually fine. For anything small, owner-operated, chef-driven, or artisan, treat Google Maps hours as a starting hypothesis, not a fact, and verify through the official site, a phone call, or Instagram before building an itinerary slot around it. Holiday hours in particular are the single most under-maintained field across all of these sources; assume any date within a week of a public holiday needs manual verification regardless of source.

---

## 6. Planner-facing checklist

Use this when assembling a day-by-day itinerary, not just when checking a single venue.

1. **Cluster by neighborhood AND by open-day simultaneously.** A geographically efficient cluster is worthless if half the venues in it share the same closure day; check both axes before locking a day's route.
2. **Maintain a running "what is closed today" list per day of the trip**, built from the weekly-pattern tables in Section 2 plus the holiday-cluster table in Section 3, cross-referenced against the actual trip dates.
3. **Front-load closure-risky anchors.** Put any single-point-of-failure destination (a specific must-see museum, a hard-to-book restaurant) earlier in the trip rather than on the last available day, so there is still a make-up slot if it turns out to be closed, sold out, or under renovation.
4. **Keep one alternate per day**, not per stop: a fallback neighborhood, museum, or meal option that has looser hours (or is open 7 days) that a day can pivot to if the planned anchor falls through.
5. **Check the specific date against the holiday tables even when the destination country's headline holidays seem irrelevant to the traveler.** Local fiestas, ordinal maintenance closures, and religious-calendar shifts (Ramadan, Nyepi, Diwali) affect operating hours even for travelers who have no personal connection to the observance.
6. **Re-verify hours 48 hours before each day actually happens**, not just once during initial planning. This catches: (a) irregular-hours venues that changed since booking, (b) holiday-hours updates that only get posted close to the date, (c) weather-driven seasonal closures (beach clubs, mountain passes, ferries) that can flip in days rather than months.
7. **Treat "irregular, check IG"-class venues as provisional until the 48-hour re-check**, and do not anchor a day's structure around them; treat them as a bonus stop if confirmed open, not as the spine of the day.
8. **For any Monday-holiday itinerary day, explicitly check the day-after-holiday closure risk** (Section 1.11, Section 3) for museums and similar venues in that country, since this specific failure mode is easy to miss when only checking "is today a holiday."

### 6.1 Worked mini-example

A 3-day city itinerary that includes one flagship museum, one wholesale-market breakfast stop, one fine-dining dinner, and one artisan-workshop visit, landing on a Monday-Tuesday-Wednesday.

| Day | Risk check before locking the plan | Placement decision |
|---|---|---|
| Monday | Flagship museum: confirm whether this specific institution is Monday-closed (global default) or one of the Tuesday-closure exceptions (Section 2.1a); wholesale market: confirm it isn't the market's own weekly closure day | If the museum turns out to be Monday-closed, this is the day to do the market breakfast and artisan workshop instead, saving the museum for Tuesday |
| Tuesday | Museum (now confirmed open); fine-dining dinner: confirm the restaurant isn't on its Sunday/Monday dark days (it likely reopened by Tuesday) and check for an August-closure or Ramadan-hours flag if the trip falls in those windows | Front-load the museum here since it was the closure-risky anchor; dinner booking reconfirmed 48 hours out per item 6, above |
| Wednesday | Artisan workshop: confirm appointment-only booking is actually held (not just requested); check it isn't the venue's periodic (e.g., "3rd-Wednesday") maintenance closure day | Kept as the last day specifically because it was the easiest to move if the appointment fell through; alternate (a second neighborhood or a flexible-hours shop) is on standby |

This mirrors items 1-8 directly: the anchor (museum) got front-loaded once its actual closure day was confirmed rather than assumed, the day-list was cross-checked against both weekly patterns and any holiday-cluster dates the trip might touch, and each day carried a named alternate rather than a single point of failure.
