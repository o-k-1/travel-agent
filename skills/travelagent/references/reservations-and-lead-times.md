# Reservations and Ticketing Lead Times: Worldwide Reference

Region-agnostic reference for tagging and sequencing every bookable item in a trip: restaurants, museums, permits, tours, transport, sporting events, festivals. Built for planning trips anywhere (Japan, Italy, Peru, Vietnam, Portugal, etc.). Japan and a handful of other markets appear as line items, not as the organizing frame.

Last verified: 2026-08-17. Corporate ownership of booking platforms changes fast (mergers, shutdowns, rebrands); ticketing rules for attractions change at least annually. Re-verify anything tagged "(unverified)" and re-check official URLs before relying on this for an active trip.

**Contents:** (1) Lead-time tiers and tagging taxonomy, (2) booking platform catalog by region, (3) non-restaurant reservation systems that catch travelers out, (4) cancellation and deposit norms, (5) practical planner rules, (6) reservation-blocker gotchas, plus a quick-reference cheat sheet at the end.

---

## 1. Lead-Time Tiers (Tagging Taxonomy)

Tag every bookable item in an itinerary with one of these tags. Sequence the whole trip by tag: book `RES:3-6mo` and `RES:lottery` items first (they often gate the trip's dates), then `RES:1-2mo`, then `RES:2-4wk`, then fill `RES:1wk`/`RES:same-day` items once on the ground.

| Tag | Typical booking window | What falls here |
|---|---|---|
| `RES:3-6mo` | 3-6 months, sometimes a year+ | 2-3 Michelin-star restaurants, single-counter omakase/sushi (8-10 seats), El Celler de Can Roca/Noma/Central-tier destination dining; Inca Trail permits (recommended 6-8 months, sells out in days for peak season); some traditional ryokan with kaiseki (especially during momiji/sakura season); polar expedition cruises; luxury safari camps in East/Southern Africa during peak season; hunting/wildlife permits in some African countries |
| `RES:1-2mo` | 30-60 days | Most 1-star Michelin and well-known fine dining; Eiffel Tower summit (60 days); Uffizi Gallery peak dates (30-60 days); Rijksmuseum (~90 days but effectively needed 1-2mo out); Neuschwanstein Castle (~8 weeks); Anne Frank House (6 weeks, released weekly); Sagrada Familia (~60 days); popular walking/food tours with small group caps; Everest Base Camp trek permits and popular Himalaya trekking permits; some national park backcountry permits (Zion quarterly release) |
| `RES:2-4wk` | 2-4 weeks | Mid-tier tasting-menu restaurants; Alhambra (90-day window but effectively fine at 2-4wk outside peak); Borghese Gallery (initial batches 2-3mo, but many slots at 10 days so 2-4wk is the safe zone); Colosseum Underground guided add-ons; popular cooking classes; small-boat day cruises; NPB baseball and sumo tickets (roughly 1mo out); car rentals in high season; popular half-day tours |
| `RES:1wk` | 3-10 days | Standard restaurants in high season; Acropolis (book 3-7 days ahead in peak, longer window technically open); most scenic train seat reservations (Rocky Mountaineer-tier trains want more, but many regional scenic rail seats open ~1wk-1mo); ferry crossings in shoulder season; wine tasting appointments at boutique wineries; spa treatments at popular hotels |
| `RES:same-day` / `RES:day-of-timed-entry` | Hours to same day | Many neighborhood restaurants outside peak; walk-up timed-entry slots released daily (Colosseum Underground daily 8:45am release, Petra day-of entry); casual museum entry in most cities; bike/scooter rentals; most city walking tours; hop-on-hop-off passes |
| `RES:walk-in` | No booking; queue on arrival | Most casual/street food, izakaya, trattorie outside tourist centers, ramen shops, tapas bars, cafes, markets; note queue behavior below |
| `RES:lottery` | Ballot, results days-to-weeks later | Kyoto Imperial Household Agency villas (Katsura, Shugakuin, Sento; apply 3 months out, lottery if oversubscribed); Yosemite wilderness permits (24-week advance lottery); Zion Angels Landing and The Narrows top-down (seasonal lottery + daily lottery); some marathon/running event entries (Tokyo Marathon, NYC Marathon, Boston qualifying); popular festival tickets in Japan (some fireworks viewing areas); certain safari/park entry quotas in high-demand African reserves |
| `RES:concierge-only` | No public booking path | Ultra-exclusive counters in Japan that only take bookings via a known regular or hotel concierge (some sushi-ya, some kappo); members-only clubs; some Michelin 3-star rooms that only accept repeat guests or referrals; certain hunting lodges; some private-island resorts |

**Queue behavior for `RES:walk-in`:** note expected wait (e.g., "20-40 min at peak lunch," "arrive by 11:30am to beat the noon rush," "queue forms 45 min before doors open"). For genuinely popular walk-in-only spots (many top ramen shops, some izakaya), treat opening time as the reservation: arriving at opening or immediately before is the de facto booking strategy.

### Tier breakdown by venue type

**`RES:3-6mo`**
- Restaurants: 2-3 Michelin-star dining rooms, single-counter omakase/sushi with 8-12 seats, tasting-menu destinations that anchor a trip (Noma-tier, Central, El Celler de Can Roca, Alinea).
- Museums/timed entry: not typical at this tier; almost all timed-entry museums release inside 6 months.
- Permits: Inca Trail (Classic 4-Day), Kilimanjaro peak-season slots via operator, gorilla trekking permits in peak season.
- Tours: polar/expedition small-ship cruises, marquee named scenic trains (Venice Simplon-Orient-Express-tier), multi-week private guided itineraries.
- Sporting events: Olympics and World Cup ballots open in this window (technically 12-18 months, but the effective "must apply now" moment often lands here relative to trip planning), Wimbledon public ballot.
- Transport: none typically needs this much lead time; flights are a separate pricing/availability question, not a reservation-lead-time one.

**`RES:1-2mo`**
- Restaurants: most 1-star Michelin, well-reviewed destination restaurants without single-digit seating, popular hotel-anchored fine dining.
- Museums/timed entry: Eiffel Tower summit, Uffizi (peak dates), Rijksmuseum, Neuschwanstein, Anne Frank House, Sagrada Familia, Louvre and Versailles (peak-season morning slots), British Museum special exhibitions.
- Permits: Everest Base Camp and popular Himalaya trekking permits (arranged via agency), some Zion backcountry (quarterly release lands here relative to trip planning), Galapagos land-based tours.
- Tours: small-group specialty food/walking tours with hard caps (under 12 people), popular multi-day guided treks.
- Sporting events: Six Nations club/member allocations, F1 general sale for marquee circuits.
- Transport: seat reservations on the most popular scenic-rail routes in peak season; ferry vehicle/cabin space for summer Mediterranean or Scandinavian crossings.

**`RES:2-4wk`**
- Restaurants: mid-tier tasting-menu rooms, well-known but not landmark fine dining.
- Museums/timed entry: Alhambra and Borghese Gallery outside their earliest release windows, Colosseum Underground guided add-ons.
- Permits: none typically gate at this tier; most permit systems are either much longer lead (lottery/quota) or same-day/no-permit.
- Tours: popular cooking classes, small-boat day cruises, half-day guided excursions in high season.
- Sporting events: NPB baseball, sumo tournament tickets (roughly one month before each tournament), Six Nations general public sale.
- Transport: high-season car rental in tourist-heavy regions (inventory, not just price, can run out); regional scenic-rail seats outside the most famous routes.

**`RES:1wk`**
- Restaurants: standard well-regarded restaurants in high season, hotel restaurants during a citywide event or conference.
- Museums/timed entry: Acropolis in peak season (technically bookable further out, but 3-7 days is the practical planning window).
- Permits: not typical; most permit systems are either much longer lead or day-of.
- Tours: boutique winery tastings, private guide bookings for a single day, spa treatments at in-demand hotels.
- Sporting events: general resale/secondary tickets for events that didn't sell out in earlier windows.
- Transport: most regional/mainline scenic-rail seat reservations, ferry crossings in shoulder season.

**`RES:same-day` / `RES:day-of-timed-entry`**
- Restaurants: many neighborhood restaurants outside peak season and outside the most touristed centers.
- Museums/timed entry: Colosseum Underground's daily 8:45am release, Petra's day-based (non-timed) entry, casual/lower-demand museums in most cities.
- Permits: Angkor Wat pass (buyable a day or even hours ahead), most urban park/garden entry.
- Tours: hop-on-hop-off passes, most city walking tours, bike/scooter rentals.
- Sporting events: minor-league or lower-demand fixtures with abundant day-of inventory.
- Transport: most urban public transit day passes, many short-hop domestic ferries.

**`RES:walk-in`**
- Restaurants: most street food, izakaya, trattorie outside tourist centers, ramen shops, tapas bars, cafes, food markets.
- Museums/timed entry: rare, but some smaller regional museums and churches have no ticketing system at all.
- Permits: none.
- Tours: none (by definition, a walk-in has no tour structure).
- Sporting events: none (all ticketed sporting events require some form of advance purchase).
- Transport: many local buses, trams, and short ferry hops sold on board.

**`RES:lottery`**
- Restaurants: rare, but a handful of ultra-in-demand pop-ups and chef residencies use a lottery/raffle model instead of first-come booking.
- Museums/timed entry: Kyoto Imperial Household Agency villas (Katsura, Shugakuin, Sento) when oversubscribed.
- Permits: Yosemite wilderness permits (24-week advance lottery), Zion Angels Landing and The Narrows top-down (seasonal and daily lotteries).
- Tours: none directly, though tour operators sometimes hold their own allocation lotteries for extremely limited permits.
- Sporting events: Wimbledon public ballot, Olympics and World Cup ticket ballots, some marathon entries (Tokyo, NYC, Boston qualifying/lottery fields).
- Transport: none typically.

**`RES:concierge-only`**
- Restaurants: ultra-exclusive counters that only take bookings via a known regular or a hotel concierge with an existing chef relationship (some sushi-ya, some kappo, a subset of Michelin 3-star rooms).
- Museums/timed entry: rare, though some private collections and palace wings are viewable only via a private arrangement.
- Permits: some hunting permits and private-land access.
- Tours: bespoke private guiding arranged through a destination management company rather than any public booking channel.
- Sporting events: rare, though some private box/hospitality access at marquee events is arranged only through a corporate or club relationship, not public sale.
- Transport: private jet charter and some superyacht charter arrangements function this way, though these are outside the scope of typical trip planning.

### Notes on how the tiers interact

- **A single trip usually spans all seven tiers.** A two-week Japan or Italy trip will typically have one or two `RES:3-6mo` anchors, four or five `RES:1-2mo`/`RES:2-4wk` museum or dining bookings, a handful of `RES:1wk` items, and the rest filled in day by day. Building the tag list first, before building the day-by-day itinerary, is what prevents an anchor reservation from being discovered too late.
- **Tiers are directional, not absolute.** The same restaurant can move tiers with the season: a mid-tier trattoria that's `RES:walk-in` in November can become effectively `RES:1wk` in August in a heavily touristed city center. Re-tag by season, not just by venue category.
- **Release-moment items behave differently from rolling-window items.** Some systems (Anne Frank House's weekly Tuesday release, Ghibli Museum's 10th-of-the-month release, Colosseum Underground's daily 8:45am release) open a fixed batch at a fixed instant and can sell out within minutes. Others (Rijksmuseum's ~90-day rolling window, most restaurant platforms) simply add one more day of availability every day, with no single moment of scarcity. Flag release-moment items distinctly (e.g., `RES:2-4wk[release:tue-10am]`) so the traveler knows to be online at that exact time rather than "any time in the window."
- **A lottery result can arrive after other bookings are already locked in.** Because `RES:lottery` outcomes are unknown at the time of entry, avoid buying non-refundable flights or hotel nights that assume a lottery win until the result is confirmed, where the calendar allows it.

---

## 2. Booking Platform Catalog by Region

Corporate ownership of these platforms consolidates and shifts often (mergers, shutdowns). Treat brand names as durable; treat "who owns whom" as volatile and unverified unless independently reconfirmed close to travel dates.

### North America

| Platform | URL | Covers | Notes |
|---|---|---|---|
| Resy | resy.com | US fine dining/hot tables, growing international (London, Paris, Tokyo, Sydney) | American Express-backed; Amex Platinum cardholders get early/exclusive access to some releases. (unverified) Resy absorbed Tock into a single platform in 2026 with the Tock consumer app decommissioned: reconfirm before relying on a Tock-specific link. |
| Tock | (formerly exploretock.com) | Prepaid tasting-menu/ticketed dining, wineries, tours | (unverified) Reported folded into Resy in 2026; if a restaurant's site still links to Tock, the link may now redirect to Resy. Verify per-venue. |
| OpenTable | opentable.com | Largest global footprint by venue count, strong in suburbs/smaller cities and outside the US (UK, Canada, Mexico, Australia, France, Japan, Germany) | Booking Holdings-owned. Best default first stop when a venue isn't on Resy. |
| SevenRooms | sevenrooms.com | US, growing enterprise/hotel-group and Middle East/APAC presence (Dubai, Riyadh, Singapore, Hong Kong) | Primarily a reservation/CRM backend restaurants license; consumer-facing booking widget is embedded on the restaurant's own site rather than a browsable marketplace. (unverified) Reported DoorDash acquisition in 2025: reconfirm. |
| Yelp Reservations | yelp.com | Mid-market US restaurants, especially outside major fine-dining markets | Free-tier and low-cost alternative many independent restaurants use instead of Resy/OpenTable. |

### Europe (Continental)

| Platform | URL | Covers | Notes |
|---|---|---|---|
| TheFork | thefork.com (regional domains, e.g. lafourchette.com in France, eltenedor.es in Spain) | Largest European marketplace: France, Spain, Italy, Portugal, Benelux, Switzerland, Nordics | TripAdvisor-owned historically; (unverified) reports of a 2026 acquisition by American Express: reconfirm. Often shows discounted "TheFork Pay" pricing at off-peak times. |
| Zenchef | zenchef.com | France, Benelux, DACH (Germany/Austria/Switzerland), growing Iberia/Italy via 2025 CoverManager merger | European-owned, commission-free/flat-fee model; increasingly the default booking widget embedded directly on independent restaurants' own websites across France and the Netherlands. |
| Quandoo | quandoo.com | Historically Germany, Austria, Switzerland, Italy, UK, Netherlands, Turkey | (unverified) Multiple 2026 reports indicate Quandoo is winding down / shutting consumer operations by end of 2026. If a restaurant page links to Quandoo, verify the link still resolves before relying on it; have a phone/email fallback ready. |
| Direct email/phone norm (Italy, Spain, rural France) | n/a | Many trattorie, agriturismi, and family-run restaurants outside major cities | No platform at all is normal. Email in the local language (or ask your hotel to call) is the standard method; expect a slow or informal confirmation, sometimes just "va bene, ci vediamo" with no written confirmation. |

### United Kingdom

| Platform | URL | Covers | Notes |
|---|---|---|---|
| OpenTable | opentable.co.uk | Broad UK coverage, especially chains and mid-market | |
| SevenRooms | (venue-embedded, no central UK marketplace) | Higher-end London groups | UK is SevenRooms' largest non-US customer base by some measures; book via the restaurant's own website widget. |
| Dishcult | dishcult.com | (unverified) Newer UK-focused discovery/booking layer, smaller scale | Verify current activity before relying on it. |
| ResDiary | resdiary.com | UK and Ireland independents, integrates into many restaurant websites | Common white-label backend; consumer sees it as a widget on the venue's own site, not a standalone marketplace most travelers browse. |

### Japan

| Platform | URL | Covers | Notes on foreigner access |
|---|---|---|---|
| Tabelog | tabelog.com (English: tabelog.com/en) | Largest Japanese restaurant database and review site; direct booking for a growing subset of listings | English/multilingual app now supports booking without a domestic Japanese phone number for many venues; the English-interface booking flow can carry a small per-person system fee (in the low hundreds of yen). Many listed restaurants remain phone-only or Japanese-app-only. |
| OMAKASE (omakase.in) | omakase.in | High-end sushi and kaiseki counters, English interface | Accepts international phone numbers for most listings; a subset of ultra-exclusive counters still restrict bookings to Japanese numbers. |
| Pocket Concierge | pocket-concierge.jp | Premium/tasting-menu dining, English interface, American Express-linked | Most bookings require upfront prepayment for the course, which removes in-restaurant payment friction and no-show risk. |
| TableCheck | tablecheck.com | Wide restaurant coverage, English interface, generally no platform booking fee | Considered the most foreigner-friendly of the Japanese platforms; supports international numbers and email-first confirmation. |
| Ikyu (一休.com) | ikyu.com | Luxury hotel restaurants and hotel-linked dining, ryokan | Primarily Japanese-language; email verification fallback exists for numbers that can't receive Japanese SMS. Browser translation (Chrome) makes it workable for non-readers. |
| Hotel-concierge-only norm | n/a | Many single-counter sushi-ya, small kappo, some 3-star kaiseki rooms | Long-standing norm: certain restaurants take reservations only through a known regular, a Japanese-speaking intermediary, or a luxury hotel concierge who has an existing relationship with the chef. No public platform bypasses this; book the hotel first if a specific restaurant is a trip anchor. |

### Korea

| Platform | URL | Covers | Notes on foreigner access |
|---|---|---|---|
| CatchTable (CatchTable Global) | catchtable.co.kr / catchtable global app | Fine dining, omakase, popular casual restaurants | Global version explicitly built for foreign tourists: sign up via email/Google/Apple ID, no Korean phone number required, accepts international Visa/Mastercard/Amex, multi-language interface. Best first stop for reservations in Seoul/Busan. |
| Naver (Naver Map / Naver Booking) | map.naver.com | Broadest local restaurant coverage including neighborhood spots not on CatchTable | Historically required a Korean phone number; (unverified) reports of a 2026 passport-plus-face-scan verification path that removes this requirement, though manual review can reportedly take days, so complete it before departure, not on arrival. |

### China

| Platform | URL | Covers | Notes on foreigner access |
|---|---|---|---|
| Dianping (大众点评) | dianping.com / app | Dominant restaurant discovery and reservation/queue app | App has an English-language settings toggle; registration with an international phone number is supported in recent versions per (unverified) reports, but SMS delivery to foreign numbers is unreliable. WeChat Mini-Program version offers in-app translation overlay as a workaround. Some venues' queue system ("排队") still expects a Chinese number; giving the hotel's front-desk number as a placeholder is a common workaround. |
| Meituan | meituan.com | Alternative/overlapping coverage to Dianping, stronger for delivery and group-buy deals | Chinese-language-first; less useful for a first-time foreign visitor than Dianping's English mode. |
| WeChat / Alipay direct | n/a | Payment and mini-program layer underneath most China bookings | Set up international-card linking and complete real-name/passport verification in Alipay or WeChat before arrival; verification can be blocked or delayed once in-country. |

### Southeast Asia

| Platform | URL | Covers | Notes |
|---|---|---|---|
| Chope | chope.co | Singapore, Bangkok, Jakarta, Manila, Hong Kong, Kuala Lumpur | Strong in Singapore particularly; increasingly integrated into Grab's app as a "Dine Out"-style feature in some markets (Thailand). |
| Eatigo | eatigo.com | Thailand, Singapore, Malaysia, Philippines | Time-based discount model (deeper discount for off-peak seating times); useful for budget-conscious flexible dining. |
| Direct WhatsApp/LINE | n/a | Widespread across Vietnam, Thailand, Indonesia, and smaller operators everywhere in the region | For anything not on Chope/Eatigo (most street food, most small local restaurants, many boutique hotels' in-house restaurants), a WhatsApp or LINE message with your hotel's help, in the local language, is the norm. |

### Latin America

| Platform | URL | Covers | Notes |
|---|---|---|---|
| Meitre | meitre.com | High-end/50-Best-list restaurants, strongest in Argentina and Colombia | Positioned as a fine-dining-focused booking layer; (unverified) reported as "coming soon" in Mexico and Peru as of early 2026: check current coverage before relying on it there. |
| OpenTable | opentable.com.mx and similar regional pages | Mexico (strongest), expanding presence in Argentina, Colombia, Peru | |
| Direct WhatsApp | n/a | Majority of restaurants across the region outside major-city fine dining | WhatsApp is the default communication channel for confirmations, reminders, and direct booking requests throughout Latin America; expect to message in Spanish or Portuguese, or ask your hotel to relay. |

### Middle East

| Platform | URL | Covers | Notes |
|---|---|---|---|
| SevenRooms | (venue-embedded) | Dubai, Abu Dhabi, Riyadh (including NEOM-linked developments), Doha | Strong enterprise presence in the region's luxury hospitality groups; book via the restaurant or hotel's own site. |
| Direct phone/WhatsApp/concierge | n/a | Majority of standalone restaurants outside big hotel groups | Hotel concierge booking is especially common and often expected for higher-end venues; a direct call is standard for local family-run restaurants. |

### Australia / New Zealand

| Platform | URL | Covers | Notes |
|---|---|---|---|
| Now Book It | nowbookit.com | Large flat-fee incumbent across Australia and NZ, especially independent and multi-site groups | Flat monthly subscription model (no per-cover fee) makes it popular with venues that already drive their own traffic; still book directly through the restaurant's own site widget. |
| SevenRooms | (venue-embedded) | Larger groups, hotels, "eatertainment" venues | |
| OpenTable | opentable.com.au | Broad discovery-driven coverage, especially newer venues and tourist areas (Sydney CBD, Queenstown) | |
| First Table | firsttable.co.nz / .com.au | NZ- and AU-specific first-visit discount booking model | Niche but genuinely useful for trying new restaurants at a discount on the first visit. |

### South Asia (India)

| Platform | URL | Covers | Notes |
|---|---|---|---|
| EazyDiner | eazydiner.com | Premium/fine dining, 5-star hotel restaurants across major Indian cities | "EazyDiner Prime" membership yields the deepest discounts at high-end hotel restaurants (Taj, Marriott, Oberoi groups); best first stop for upscale dining. |
| Swiggy Dineout | dineout.co.in (now under Swiggy) | Mass-market discovery, mid-range restaurants, broadest city coverage | Strong seasonal discount events; more focused on volume/value dining than fine dining. |
| Zomato (Dining) | zomato.com | Largest overall restaurant database, strongest for casual/local discovery | Good for finding smaller local spots not on the other two platforms; "Zomato Gold" membership layers in discounts. |

### Africa

| Platform | URL | Covers | Notes |
|---|---|---|---|
| Direct phone/email/hotel concierge | n/a | Majority of standalone restaurants across the continent outside a handful of major-city fine-dining scenes (Cape Town, Johannesburg, Nairobi, Lagos, Marrakech) | No dominant continent-wide platform exists; safari lodges and high-end city restaurants are typically booked through the lodge/hotel directly or via a specialist travel agent, not a consumer app. |
| Dineplan / Quicket (South Africa) | (unverified) dineplan.com | Some Cape Town/Johannesburg restaurants | Regional, not continent-wide; verify current adoption before relying on it as a primary channel. |

**Practical cross-region rule:** if a country-specific platform demands a local phone number, local ID, or local payment method you don't have, the fallback order is: (1) try the platform's international/English mode if one exists, (2) ask your hotel concierge to book by phone in the local language, (3) email the restaurant directly, (4) as a last resort use a paid concierge/travel-agent service. Never assume a workaround (fake number, hotel's number, etc.) will hold for a high-value reservation; confirm with the venue that it will actually reach you.

---

## 3. Non-Restaurant Reservation Systems That Catch Travelers Out

### Timed-entry museums and monuments

| Site | Country | Official booking portal | Typical lead time / release pattern |
|---|---|---|---|
| Vatican Museums / Sistine Chapel | Italy | tickets.museivaticani.va | Baseline 60 days; during high-demand periods (e.g., Jubilee years) tickets have appeared 3-6 months out. Nominative tickets since Aug 2024 (ID required at entry). Morning slots in peak season (Apr-Oct) can sell out 3-4 weeks ahead. |
| Alhambra | Spain (Granada) | tickets.alhambra-patronato.es | ~90-day rolling window; nominative (passport/ID number required at booking and entry). Palacios Nazaríes slots sell out first. |
| Sagrada Familia | Spain (Barcelona) | sagradafamilia.org/en/tickets | ~60-day window; tower access (Nativity or Passion facade) sells out well before general admission. |
| Uffizi Gallery | Italy (Florence) | tickets.uffizi.it (managed by CoopCulture) | Book 1-2 months ahead for peak dates; tickets are nominative (name must match ID exactly, no changes after purchase). |
| Borghese Gallery | Italy (Rome) | tosc.it (official ticketing partner) | Released in waves: initial batch 2-3 months out, additional batch 10 days out. Reservations mandatory even for free-admission days; strict 2-hour entry slots. |
| Cenacolo Vinciano / The Last Supper | Italy (Milan) | cenacolovinciano.org / official ticket vendor (e.g. vivaticket) | Released in quarterly batches (roughly 3 months ahead) plus small weekly releases. Nominative and non-transferable; arrive 30 min early for ID check. |
| Acropolis | Greece (Athens) | hhticket.gr | Mandatory 2-hour timed slots since 2024. Technically bookable well ahead, but 3-7 days out is enough outside extreme peak. Combination multi-site ticket discontinued in 2025 (unverified): check whether separate tickets are needed per site. |
| Machu Picchu (general entry) | Peru | tuboleto.cultura.pe (Peru Ministry of Culture) | 4-6 weeks for shoulder season, 2-3 months for peak (Jun-Aug). Daily capacity caps mean popular circuits/time slots sell out. |
| Huayna Picchu | Peru | tuboleto.cultura.pe (add-on to Machu Picchu ticket) | Book 3-4 months ahead; daily capacity is separately and strictly limited (roughly 350-400 spots/day split across two entry groups), sells out well before general Machu Picchu entry. |
| Inca Trail permits (Classic 4-Day) | Peru | Cannot book directly; must go through a licensed tour operator | Book 6-8 months ahead for Jun-Aug; permits for peak months have reportedly sold out within 24-48 hours of the annual release. Trail closed every February for maintenance. |
| Petra | Jordan | visitpetra.jo / petrapass.jo (or via Jordan Pass) | E-tickets valid up to several months from issuance; no mandatory timed entry for standard daytime visits. "Petra by Night" is a separate ticket typically bought in person a day or two ahead, not far in advance. |
| Angkor Wat / Angkor Archaeological Park | Cambodia | angkorenterprise.gov.kh | No timed entry; multi-day passes valid within a rolling window (3-day pass valid over 10 days, 7-day pass over 30 days). Buy a few days ahead or even same-day; low sellout risk. |
| Kyoto Imperial Household Agency sites (Katsura Imperial Villa, Shugakuin Imperial Villa, Kyoto Sento Imperial Palace) | Japan | sankan.kunaicho.go.jp | Online applications open at the start of the month, 3 months before the visit month; a lottery is held if oversubscribed. In-person same-day numbered tickets are also distributed at each site each morning on a first-come basis. Passport required; minimum age 18 for the villas and Sento Palace. Kyoto Imperial Palace itself needs no advance booking. |
| Ghibli Museum | Japan (Mitaka, Tokyo) | Lawson Ticket (English portal) / ghibli-museum.jp | Tickets for a given month go on sale on the 10th of the prior month; a virtual queue system is used and popular slots sell out within the release window. Non-refundable, name-tied; the lead booker must be present with a passport for the whole group to enter. |
| teamLab Planets / teamLab Borderless | Japan (Tokyo) | Official teamLab site or authorized resellers | Released roughly 2-3 months ahead on a rolling basis; no lottery, first-come first-served; popular morning slots sell out weeks ahead. |
| Alcazar of Seville | Spain | alcazarsevilla.org | (unverified) Generally book 2-4 weeks ahead; Royal Apartments add-on has separate, more limited timed slots that sell out faster. |
| Neuschwanstein Castle | Germany | hohenschwangau.de (official ticket center) | ~8 weeks recommended; a limited allotment of same-day tickets is sold at the on-site ticket center from 8:00am but often requires hours of queuing. |
| Eiffel Tower (summit) | France (Paris) | toureiffel.paris | 60 days for summit/elevator tickets, 30 days for stairs-to-second-floor tickets; released daily at midnight Paris time. |
| Colosseum Underground / Full Experience | Italy (Rome) | ticketing.colosseo.it (official) | 30-day window, released daily around 8:45am Rome time. Nominative; names of all visitors required at booking. |
| Nikola Tesla Museum | Serbia (Belgrade) | (unverified) nikolateslamuseum.org | Group/guided-tour timing generally bookable with a few days' notice; verify current system before travel. |
| Rijksmuseum | Netherlands (Amsterdam) | rijksmuseum.nl | ~90-day rolling window; every visitor needs a specific start-time slot even though the museum is rarely fully sold out outside marquee exhibitions. |
| Anne Frank House | Netherlands (Amsterdam) | annefrank.org | Fixed 6-week lead time; a full week's tickets release every Tuesday at 10:00am (CET/CEST). Popular midday slots have reportedly sold out within minutes. No on-site ticket office and no waiting list if sold out. |
| Louvre | France (Paris) | ticket.louvre.fr | Tickets released roughly 90 days (3 months) ahead; book 2-3 weeks ahead for peak-season (Apr-Oct) morning slots, 1 week is enough off-peak. Timed entry is mandatory for every visitor including museum-pass holders. |
| Palace of Versailles | France (Versailles) | billetterie.chateauversailles.fr | Released 3+ months ahead; book 2 weeks ahead for the Palace interior's high-demand morning slots, 1 week for the Estate of Trianon. A bundled "Passport" ticket (not a standalone Palace-only ticket) is required for interior access. |
| British Museum | UK (London) | britishmuseum.org | General admission released roughly 4 months ahead; 2 weeks is enough for prime slots, 1-2 days for off-peak. Major loan exhibitions (special ticketed shows) can require booking the moment tickets are released, months ahead. |
| Taj Mahal | India (Agra) | asiagracircle.in (Archaeological Survey of India official site) | Standard entry bookable within days; timed to a 3-hour single-entry window from the moment of entry, not a fixed clock slot. Closed to general visitors on Fridays (open only for afternoon prayers). Night viewing (full moon and the two nights either side) is a separate ticket that must be booked at least 24 hours ahead and is unavailable on Fridays and during Ramadan. |

### National park permits, quotas, and backcountry access

| System | Country | Lead time pattern |
|---|---|---|
| Yosemite wilderness permits | USA | 60% via 24-week-ahead weekly lottery; 40% released 7 days ahead first-come-first-served on recreation.gov. |
| Zion general backpacking permits | USA | Quarterly release windows (opens the 5th of the month, roughly one quarter ahead), plus 50% held back for in-person day-before walk-up. |
| Zion Angels Landing / The Narrows (top-down) | USA | Seasonal lottery opens several months ahead (e.g., a summer-season lottery opening in spring) plus a daily/day-before lottery for last-minute spots. |
| Everest Base Camp / Himalaya trekking permits | Nepal | Permits (TIMS, national park entry) typically arranged by the trekking agency; book the trek itself 2-4 months ahead in peak season (Mar-May, Sep-Nov). |
| African safari park entry / high-demand reserve permits | Various (Rwanda gorilla trekking, some East/Southern Africa reserves) | (unverified) Gorilla trekking permits in Rwanda/Uganda commonly need booking 3-6+ months ahead in high season; verify current permit cost and lead time directly with the park authority or operator, as these change often and permits are capacity-limited per day. |
| Kilimanjaro climbing permit | Tanzania | Conservation/entry fees set by TANAPA and collected via the operator, not booked directly by the traveler; book the climb itself 6-9 months ahead for peak season to secure preferred dates and a reputable operator. Fees include a daily conservation fee plus separate camping/hut, rescue, and forest fees, all subject to change. |
| Galapagos Islands entry | Ecuador | National park entry fee is paid in person on arrival (historically cash-only) at Baltra or San Cristóbal airport; a separate transit control card must be registered online before arrival from the mainland. Book cruises 10-12 months ahead for peak season (Dec, Jun-Aug); land-based tours need 4-6 months. |
| Torres del Paine | Chile | Reservations split across multiple official portals (park entry authority plus separate campsite/refugio operators); book 6-8 months ahead for peak season (Dec-Feb). The park has moved toward route-specific ticketing (matching the ticket to the exact circuit walked), so confirm the correct ticket type for the planned route, not just a generic park-entry ticket. |

### Ferry, scenic rail, and guided-only access

| Type | Lead-time guidance |
|---|---|
| Scenic/named trains (e.g., Rocky Mountaineer-tier, Bernina Express panoramic cars, Venice Simplon-Orient-Express) | Marquee named trains: 2-6 months ahead in peak season. Standard reserved-seat scenic rail (many European regional/mainline trains): often opens 1-3 months ahead, comfortably bookable 1-4 weeks out except around major holidays. |
| Ferries with vehicle or cabin reservations (Greek islands, Adriatic crossings, Scandinavian ferries) | Foot-passenger tickets are frequently walk-up/same-day outside peak; vehicle spaces and cabins on overnight routes should be booked weeks to a couple of months ahead in summer. |
| Guided-only sites (some caves, some archaeological sites, certain royal palace interiors) | Guided-only access typically has a smaller daily cap than self-guided sites; book as early as the general site's booking window opens, since guide slots often sell out before general timed-entry slots do. |

### Sporting events, festivals, and adventure operators

| Type | Lead-time guidance |
|---|---|
| Sumo tournaments (Japan) | Tickets go on sale about one month before each of the six annual tournaments (Jan, Mar, May, Jul, Sep, Nov); use the official English-language ticket portal to avoid the Japanese-phone-number SMS-verification barrier on domestic sites. Popular days sell out within the release window. |
| NPB baseball (Japan) | Team-specific official English ticket sites; book 1-2 months ahead for popular matchups; some in-demand games use a pre-sale lottery before general sale opens. |
| Football (soccer) matches worldwide | Big-club domestic league games: club's official membership/ticket site, often 2-4 weeks ahead for non-marquee fixtures, months ahead for rivalry/derby matches and any European competition knockout rounds. |
| Festival grandstand/reserved seating (e.g., Rio Carnival, Kentucky Derby, Edinburgh Festival marquee events, Songkran main-stage areas) | Reserved grandstand or paid-viewing seats: 2-6 months ahead for headline festivals; general free-standing viewing areas are typically walk-up but require very early arrival on the day. |
| Hot-air balloon rides (Cappadocia, Bagan, Napa, etc.) | Weather-dependent; book 1-4 weeks ahead in peak season to secure a date, but expect the operator to confirm/cancel based on morning weather, sometimes with same-day rebooking. |
| Dive trips / liveaboards | Popular liveaboards (Red Sea, Raja Ampat, Galapagos) book out 3-9 months ahead for peak season; day-boat dives are usually bookable within the week. |
| Via ferrata / guided climbs | Small-group guided climbs (e.g., Dolomites via ferrata with a guide) should be booked 1-2 months ahead in peak alpine season; solo/self-guided routes need no booking but do need a permit check in some ranges. |
| Wimbledon (tennis) | Public Ballot opens roughly 9-10 months before the tournament (a lottery, not first-come-first-served); results notified months later. Resale/official "Wimbledon Resale" queue on the day is the walk-up option. |
| Formula 1 Grands Prix | General sale for marquee races (British GP at Silverstone, Monaco, Italian GP) typically opens 9-10 months ahead; some circuits open renewal windows for existing ticket-holders even earlier. Smaller/less prestigious rounds can be bought 1-3 months out. |
| Six Nations rugby | Ticketing is decentralized by national union (RFU, WRU, SRU, FFR, FIR, IRFU); club-member allocations open 6-10 months ahead, general public sale 4-6 months ahead. Some unions (historically Italy) release earlier than others. |
| Olympics / FIFA World Cup | Ticket ballots open roughly 12-18 months ahead of the event via the organizing committee's official portal only; multiple ballot rounds are typical, with unsuccessful applicants able to re-enter later rounds. Never buy from secondary/resale sites for these events without verifying official authorized-reseller status. |

---

## 4. Cancellation and Deposit Norms

| Tier | Typical prepayment/deposit | Typical cancellation window | Notes |
|---|---|---|---|
| Ultra-fine dining / tasting-menu-only rooms | Full prepayment of the tasting menu (sometimes plus tax and gratuity) at time of booking | 7-30 days for a refund; some rooms (e.g., ultra-high-end destination restaurants) enforce 15-30 day windows | Ticket is often non-refundable but sometimes transferable to another name/date within a window. Treat as a sunk cost once booked; build the trip around this date, not the other way around. |
| High-end fine dining (1-3 star, not ticketed) | Credit card hold or partial deposit ($25-100+/person), no charge unless policy breached | 24-72 hours common; some 2-3 star rooms use 5-7 days | Late cancellation or no-show typically charges a fee per person, sometimes $100-400+ at the very top tier. |
| Mid-tier and casual restaurants | Usually no deposit; larger parties (6-8+) sometimes require a credit card to hold | 24 hours or same-day is standard when required at all | Many casual restaurants worldwide take no deposit and have no formal cancellation policy; a no-show simply means you weren't there. |
| Museums / timed-entry attractions | Full payment at booking, non-refundable in most cases (Vatican, Uffizi, Anne Frank House, Colosseum, etc.) | Effectively none: missed slot forfeits the ticket; some allow date-change for a fee if done well ahead | Because entry tickets are nearly always non-refundable, build slack (arrive early, have a backup activity) rather than relying on being able to cancel and rebook. |
| Guided tours and multi-day treks | Deposit (10-30%) at booking, balance due 30-60 days before departure is common for operator-run multi-day trips | 30-60+ days for a full/partial refund on multi-day treks and permits (Inca Trail, gorilla trekking); shorter for single-day tours (24-72 hours) | Permit-linked trips (Inca Trail, some safari permits) are frequently non-refundable once the permit itself is purchased, regardless of the tour operator's own cancellation policy. |
| Hotels tied to restaurant/attraction packages | Varies; often matches the hotel's own cancellation policy (24-72 hours for standard rate, non-refundable for prepaid rate) | Read the specific rate's terms; "confirmation required by email X days prior" is common for package inclusions like a chef's table dinner bundled into a room rate | When a hotel package includes a reservation (e.g., a set dinner), the hotel typically requires you to reconfirm attendance by email or the concierge desk a few days before, separate from the room cancellation policy. |
| Multi-day permit-linked treks (Inca Trail, Kilimanjaro, gorilla trekking) | Deposit at booking, balance 30-90 days out; the government permit fee itself is typically non-refundable once purchased by the operator on the traveler's behalf | Permit portion: none. Operator/logistics portion: 30-60+ days for partial refund, varies by operator | The permit and the tour are two different cancellation regimes bundled into one price; losing the tour deposit is common on cancellation, but losing the permit fee outright is near-universal. |
| Scenic/named trains and cruises (Venice Simplon-Orient-Express-tier, small-ship expedition cruises) | Deposit (typically 20-25%) at booking, balance 60-120 days before departure | 60-120+ days for a meaningful refund; inside that window cancellation fees escalate steeply, often to 100% inside 30 days | Treat these like a flight fare: the closer to departure, the closer to zero refund. Trip insurance is worth pricing in for these specifically. |
| Timed-entry attractions with a "reschedule, not refund" policy (some European sites) | Full payment at booking | No cash refund, but a small subset (verify per-site) allow a one-time date change if requested well before the visit date | Do not assume "non-refundable" and "non-changeable" are the same thing; check the specific site's terms, since some genuinely allow a free or low-fee date change while refusing refunds outright. |

**Regional norm summary:** North America and the UK lean toward card-hold-only policies enforced automatically by the platform (Resy, OpenTable) with fees charged programmatically. Continental Europe (especially Italy, France, Spain outside major cities) leans toward informal verbal/email confirmation with no enforced penalty, but a real social expectation to cancel if plans change. Japan and Korea's high-end dining is disproportionately prepaid-in-full given the deep advance sourcing of ingredients for tasting menus. Latin America and Southeast Asia are WhatsApp-first and rarely charge a no-show fee outside the top tier of fine dining, but a large-party no-show can quietly end future bookings at a small venue.

**"Confirmation required" pattern:** many small/independent restaurants worldwide (especially in Italy, Spain, and parts of Latin America) do not use a platform at all but expect a reconfirmation call or message 1-3 days before the reservation. If you booked by email weeks ahead and never hear back again, do not assume the table is guaranteed; reconfirm.

---

## 5. Practical Planner Rules

**Before flights are even ticketed** (these can gate which dates are viable):
1. Check `RES:lottery` items first (Kyoto villas, Yosemite/Zion permits, marathon lotteries): if the lottery calendar doesn't align with flexible travel dates, the whole trip window may need to shift.
2. Check `RES:3-6mo` anchor restaurants and Inca-Trail-style permits: if the single most important reservation of the trip needs a specific date locked in 6 months out, lock that date before booking flights around it.
3. Identify any `RES:concierge-only` items and start the hotel-concierge conversation (or find the right intermediary) as early as possible; these can take longer to arrange than a simple online booking regardless of "lead time."

**The week the trip is confirmed** (dates and flights locked):
1. Book everything in `RES:1-2mo` and `RES:2-4wk` tiers immediately if travel is inside that window; if travel is further out, set a calendar reminder for the exact release date/time (many of these use a hard release moment, e.g., "60 days out at midnight local time").
2. Book ferries, scenic-rail seats, and any guided-only site slots.
3. Buy travel insurance if any of the above involves large non-refundable prepayments.
4. Confirm passport/visa validity and any attraction-specific ID requirements (see Section 6): several of the tickets above are nominative and require the exact name and ID number matching at booking.

**Leave to the day (or the week, on the ground):**
1. `RES:walk-in` meals: scout via the platform's live availability the morning of, or simply plan arrival time around known peak/off-peak windows.
2. `RES:same-day`/`RES:day-of-timed-entry` attractions: book from the hotel the evening before or morning of.
3. Weather-dependent activities (balloon rides, some boat trips, some scenic viewpoints).
4. Spa treatments, casual bike rentals, and anything with abundant daily capacity.

**Building a backup for a single unbookable anchor:**
1. If the anchor is `RES:3-6mo` and the window has already closed (e.g., trip was booked late), check the restaurant/site directly for cancellation-released inventory; many platforms surface last-minute cancellations, and some (Resy Notify, similar features elsewhere) offer an alert/waitlist function.
2. Identify a credible second-choice at the same tier and same neighborhood/day, and book it as an immediate placeholder while continuing to watch for the anchor to open up.
3. For attraction tickets sold out at the official portal, treat authorized resellers (official tour-operator allotments, not scalper sites) as the fallback, accepting the markup, rather than arriving without a plan.
4. For hotel-concierge-only venues, ask the concierge to place your name on any waitlist as soon as you check in, even before your target date; some kitchens keep a running waitlist that gets worked through by seniority of request, not by online queue.

**Sequencing rule of thumb, end to end:**
1. Lock trip dates around any `RES:lottery` and `RES:3-6mo` anchors first.
2. Book flights and the first/last hotel nights once dates are fixed.
3. Book the rest of `RES:3-6mo` and all `RES:1-2mo` items the day dates are locked (set alerts for exact release moments).
4. Book the remaining hotel nights and any internal transport (domestic flights, scenic trains, ferries) once the day-by-day skeleton exists.
5. Book `RES:2-4wk` and `RES:1wk` items 2-4 weeks out, in descending order of how likely they are to sell out.
6. Leave `RES:walk-in` and `RES:same-day` to the ground; do not spend planning time pre-booking these, since doing so trades flexibility for no real benefit.
7. Reconfirm every prepaid/nominative item's exact name-on-booking and required ID against actual passports 1-2 weeks before departure; a typo caught early is fixable, one caught at the door is not.

**Signals that a reservation is actually the trip's real constraint (treat as a flight-ticketing gate, not a nice-to-have):**
- Daily capacity is a fixed, small number (Huayna Picchu, Inca Trail, gorilla trekking, Ghibli Museum).
- The system is a lottery/ballot with a fixed application window (Kyoto villas, Yosemite, Wimbledon, Olympics).
- The venue has a single seating per day or a single-digit number of covers (single-counter omakase, some 3-star tasting rooms).
- The permit and the trek/tour are inseparable, so missing the permit window collapses the whole multi-day plan (Inca Trail, Kilimanjaro route permits).

---

## 6. Reservation-Blocker Gotchas

Non-obvious requirements that can silently block a booking or an entry, discovered too late if not checked in advance.

| Gotcha | Where it bites | What to do |
|---|---|---|
| International Driving Permit (IDP) required before departure | Italy, Spain, Japan, and most non-EU/EEA rental situations generally; Japan in particular only recognizes the 1949 Geneva Convention format IDP (not the 1968 Vienna Convention version some countries issue) | Obtain the IDP in your home country before departure (e.g., via AAA in the US); it cannot be obtained once abroad. Carry both the IDP and your original physical license. |
| Nominative/passport-linked tickets | Vatican Museums, Uffizi, Colosseum, Cenacolo Vinciano, Alhambra, Kyoto Imperial Household Agency sites, and a growing list of others | Enter the traveler's name exactly as it appears on the passport/ID at time of booking; many portals do not allow name changes after purchase. Bring the physical passport, not just a photo, to sites that verify at entry. |
| Membership or repeat-guest requirement | Some private clubs, a subset of ultra-exclusive restaurants (sushi-ya that only take bookings from existing regulars), some golf clubs | Confirm via the hotel concierge or a local contact whether first-time outside bookings are even possible before spending time trying. |
| Residents-only or local-ID-only pricing/access | Some museums and monuments offer free/discounted entry to nationals or EU citizens only; a few sites in the Middle East and Asia have local-ID-linked ticket tiers | Do not assume a listed discounted price applies; check the eligibility fine print, since booking under a false residency claim can be denied at the door. |
| Visa-linked entry tickets | Some combined visa-and-attraction packages (e.g., certain Jordan Pass-linked Petra access, some Egypt site-and-visa bundles) | Verify whether the attraction ticket is bundled with, or independent of, the visa; buying them out of order can void the discount or require the visa product specifically. |
| Passport required at time of online booking (not just at entry) | Kyoto Imperial Household Agency applications, several nominative European tickets, Ghibli Museum (lead booker) | Have passport numbers for all travelers ready before starting the booking process; some forms time out if you have to go find the document mid-booking. |
| Closed-for-private-event risk | Palaces, historic villas, some restaurants with private dining rooms, wineries | For a trip's true "must-see" anchor, check the official site's calendar/news section close to the date for closure notices; historic properties in particular are periodically closed for private events, filming, or restoration with limited public notice. |
| Local phone number required for SMS verification | Naver (Korea, historically), many Japanese ticket platforms (Ticket Pia, Lawson Ticket), Dianping (China, partially) | Use the platform's English/international-facing product where one exists (CatchTable Global, Tickets in Japan, Dianping's English toggle); as a fallback, book via the hotel or an authorized international reseller. |
| Data-only eSIM fails phone verification | Any platform requiring SMS/call verification, most commonly in Japan and Korea | Use a voice+data-capable eSIM or a roaming-enabled physical SIM if a booking step is likely to require SMS verification; a data-only eSIM will silently fail this step. |
| 3D Secure / card verification mismatches | Japanese and Korean payment gateways especially | Notify your card issuer of international travel dates in advance and ensure the card supports 3D Secure 2.0; failed verification can cancel an otherwise-successful booking automatically. |
| Age minimums at specific sites | Kyoto Imperial Household Agency villas and Sento Palace (18+), some wine/whisky tasting experiences, certain adventure operators | Check age minimums for family trips with teenagers; a minor in the group can be turned away even with a confirmed booking. |
| Ticket resale/scalper sites masquerading as official | Nearly every high-demand attraction and event listed above | Always start from the official government/venue domain (verify the TLD and organization, e.g., a `.va`, `.gov`, or the venue's own long-standing domain) before considering an authorized reseller; unauthorized resale markups can be extreme and the ticket sometimes invalid. |
| Standard weekly closure day | Louvre (Tue), many European national museums (often Mon), Vatican Museums (most Sundays except the last Sunday of the month, which is free-and-crowded), some Japanese museums (Mon) | Check the specific site's weekly closure day before anchoring a day plan around it; closure days are not standardized across a country, let alone across a region. |
| Dress code enforcement at religious/state sites | St. Peter's Basilica, many mosques (Blue Mosque/Sultan Ahmed Mosque, Hagia Sophia), some palaces | Covered shoulders/knees are commonly enforced at the door regardless of ticket status; carry a scarf or cover-up even on a hot day, since a confirmed booking does not override the dress code. |
| Group-size caps that split a party across separate ticket transactions | Small-group guided tours, some restaurant tables at single-counter venues, permit-based treks | Book as one party in one transaction where possible; a party split across two bookings can be seated/guided separately or denied a shared time slot entirely. |
| Cash-only or local-currency-only entry fees | Galapagos National Park entry (historically cash-only on arrival), some rural site entry fees in Latin America, Africa, and parts of Southeast Asia | Carry the exact currency and denomination expected; card machines and ATMs are not guaranteed at the point of entry for these fees. |
| SIM/eSIM registration or ID requirements that gate mobile connectivity needed for a QR-code ticket | India, China, and a few other markets require ID registration for local SIM purchase | If a ticket is delivered as a QR code needing mobile data or an app to display, confirm connectivity is sorted before the day of entry, not assumed to be available at the gate. |

---

## Appendix: Quick-Reference Lead-Time Cheat Sheet

| If it's... | Tag it... | Book it... |
|---|---|---|
| A 2-3 Michelin star or single-counter omakase restaurant | `RES:3-6mo` | As soon as travel dates are set, ideally before flights |
| A major European monument/gallery in peak season | `RES:1-2mo` | The moment the release window opens (set a calendar alert for the exact time) |
| A permit-gated trek (Inca Trail, gorilla trekking) | `RES:3-6mo` / `RES:lottery` | Before flights; this often determines the trip's dates |
| A national park backcountry/day-hike lottery | `RES:lottery` | On the exact lottery-open date; results may take days-weeks |
| A mid-tier restaurant reservation | `RES:2-4wk` or `RES:1wk` | The week the trip is confirmed |
| A casual neighborhood restaurant | `RES:walk-in` or `RES:same-day` | On the ground; know the queue pattern |
| A sumo/NPB/football ticket | `RES:2-4wk` | Watch the official on-sale date; use the English-language portal where one exists |
| A hotel-concierge-only dining spot | `RES:concierge-only` | Start the concierge conversation as early as the hotel is booked |
| A scenic train, ferry, or named luxury rail journey | `RES:1-2mo` or `RES:3-6mo` (named trains) | Book alongside the rest of the internal-transport skeleton, right after flights and first/last hotel nights are set |
| A marathon, ballot-entry road race, or Olympics/World Cup ticket | `RES:lottery` | Apply the moment the ballot opens; do not lock non-refundable travel around an unconfirmed result |
| A safari lodge, gorilla trekking permit, or Kilimanjaro climb | `RES:3-6mo` | Before flights; treat the operator's booking calendar as the trip's real gating constraint |
| A weekly-closure-day museum (Louvre Tue, many EU museums Mon) | n/a (not a lead-time issue) | Check the closure day when building the day-by-day sequence, regardless of how far ahead the ticket itself was booked |

This file is a planning aid, not a live data feed: platform ownership, ticket prices, and release schedules all drift. Before finalizing a specific trip's reservation calendar, re-check the official URL for each anchor item listed here.
