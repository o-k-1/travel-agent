# Editorial Source Catalog for Trip Research

Region-agnostic reference for mining editorial and community sources when planning a trip to any city or country. Covers what to harvest, where to find it for a given city, whether it is paywalled, how to get past the paywall when no legitimate access exists, and how to weigh conflicting picks against each other.

Verified via live web search as of 2026-08-17. Anything not independently confirmed is marked "(unverified)". Where a source's WebFetch could not be reached directly in the research environment (persistent CA-certificate error on several news/travel domains), findings rely on search-engine-grounded citations instead of a direct page load; this is noted inline where it affects confidence.

---

## 0. How to use this document

A recommended harvest order for a new city, from broadest authority to narrowest niche:

1. Start with Tier 1 recurring series that actually cover the city (section 1.1): check NYT 36 Hours, Conde Nast Traveler, Eater (if the city has an active site), Michelin Guide, and The World's 50 Best. These carry the most editorial weight and the widest readership, so they anchor the rest of the research.
2. Layer in guidebooks and general travel media (section 1.2) for site-seeing depth, historical context, and neighborhood orientation that recurring series skip.
3. Pull in category-specific sources relevant to the traveler's interests: architecture (1.3), craft (1.4), menswear/retail (1.5), coffee (1.6), photography (1.7), cycling (1.8), hiking (1.9). Skip categories that do not match the trip's purpose.
4. Cross-check every English-language pick against a local-language source (section 1.10) where one exists for that country. This is the single highest-value step for catching stale or overrated picks, since local-language reviewers visit far more frequently than an outlet writing a once-a-year city guide.
5. Search Reddit and forums (section 1.11) for corroboration or contradiction, especially for anything that only appeared in one listicle.
6. Run every candidate through the source-quality rubric (section 4) before it goes into a draft itinerary.
7. Run every candidate through a freshness/closure check (section 5) before it goes into a final itinerary, and again close to departure if the itinerary was built more than a few weeks in advance.

### 1.12 Regional coverage gaps and how to compensate

The Tier 1 English-language outlets in section 1.1 are structurally biased toward North America, Western Europe, and a handful of "trend" cities in Asia (Tokyo, Bangkok, Singapore, Seoul). Coverage thins out fast for most of Africa, Central Asia, much of South Asia, and secondary cities anywhere. This is a known distortion, not a reflection of those places having less worth covering, and it should shape how much weight to put on each source tier:

- For a thinly covered city or country, do not expect a 36 Hours, Eater map, or Infatuation guide to exist at all; treat their absence as normal rather than as a signal the destination is not worth researching.
- Lean harder on local-language sources (1.10) and their real equivalents even when not named in this catalog: most countries have a dominant local review or booking platform (analogous to Tabelog or Dianping) that is far more current and far more comprehensive for that market than anything published in English. Identify it by searching `<country> most popular restaurant review app` and by asking a local-language LLM prompt for the platform name, then machine-translate its listings.
- National and city tourism board websites (typically a `.gov` or ccTLD government domain) are an underused Tier 2 source for thinly covered destinations: they are free, current, and although promotional in tone, useful for a baseline of what is officially open and operating.
- General-purpose reference sites with global reach regardless of city size (Wikipedia, Wikivoyage, UNESCO World Heritage List, OpenStreetMap-derived apps) remain reliable floor-level sources anywhere in the world, since they do not depend on an editorial outlet having assigned a writer to that city.
- Weight Reddit and forum corroboration (1.11) more heavily for thinly covered destinations, since a genuine local or a well-traveled visitor's firsthand account may be the only recent, specific source available, in the absence of a large body of editorial coverage to cross-check against.

---

## 1. Tier 1 recurring series worth systematically harvesting

### 1.1 Major newspaper and magazine travel series

| Publisher | Series / section | URL pattern (city example) | Archive / index | Paywall | 2026 notes |
|---|---|---|---|---|---|
| New York Times | "36 Hours in \<City\>" | `nytimes.com/interactive/2026/MM/DD/travel/things-to-do-[city].html` (current format); older pieces use `/travel/36-hours-[city].html` (unverified pattern, not fetch-confirmed) | No confirmed dedicated "36 Hours" tag/index page; try NYT topic pages | Metered/hard paywall | Still runs weekly to biweekly (confirmed 2026 examples: Philadelphia Jul 2026, Athens Jun 2026, Richmond Apr 2026, Raleigh Mar 2026). Companion book series is NYT x Taschen (not National Geographic): *36 Hours: 150 Weekends in the USA & Canada*, *36 Hours: 125 Weekends in Europe*, *36 Hours: World, 150 Cities*, plus a 2025 spinoff, *The New York Times: Cultured Traveler* |
| New York Times | "52 Places to Go" (annual "Where to Go") | Published early January each year under NYT Travel | Search NYT Travel front page each January | Metered/hard paywall | 2026 edition led with "Revolutionary America," then Warsaw and Bangkok |
| New York Times | Restaurant reviews | Under NYT Food/Dining, not a single URL pattern | n/a | Metered/hard paywall | Pete Wells left the chief critic role in 2024; Ligaya Mishan and Tejal Rao named co-chief restaurant critics in June 2025, the first time the role has been split and made non-anonymous |
| Conde Nast Traveler | City guides | `cntraveler.com/city-guide/[city]` (e.g. `/tokyo`, `/paris`) | Tag pages `cntraveler.com/tag/[city]` (unverified, search-synthesized, not fetch-confirmed; country-level tags unconfirmed) | Metered paywall (Conde Nast) | Gold List (annual best-hotels list) hit its 32nd edition, unveiled Dec 2025 for the Jan/Feb 2026 issue: 73 hotels across 43 countries, no carryovers from the prior year. Distinct from reader-voted "Readers' Choice Awards" |
| Conde Nast Traveler | "Best Restaurants in \<City\>", "Best Things to Do in \<City\>" | Standard editorial slugs under the main domain, no separate namespace confirmed | n/a | Metered paywall | Same editorial team as the city guides; treat as recurring but not URL-predictable |
| Eater | City maps: "The 38 Essential Restaurants", "Eater Heatmap" | `eater.com/[city]` for active sites | Each city site has its own maps index | Free | Active dedicated city sites confirmed in 2026: New York, Los Angeles, Chicago, San Francisco, Austin. Eater London has had no dedicated staff since roughly 2023 and should be treated as archived, not current. Vox Media folded several smaller city sites (Detroit, Las Vegas, San Diego, statewide Texas) into regional coverage after layoffs in Dec 2024 and Aug 2025. A claim surfaced during research that Penske Media acquired Eater from Vox Media in mid-2026 could not be corroborated and reads as unreliable; do not treat as fact without independent confirmation |
| Michelin Guide | Restaurant selections | `guide.michelin.com/en/[region]/[city]/restaurants` (e.g. `guide.michelin.com/en/tokyo-region/tokyo/restaurants`) | Country/region hubs under `guide.michelin.com/en/` | Free to browse | Bib Gourmand (good value) still active; exact filter URL unverified. Michelin Green Star is being retired globally starting June 1, 2026, replaced by an editorial (non-badge) platform called "Mindful Voices" inside the Magazine section, so do not search for a Green Star badge on new selections going forward. 2026 geographic expansion: American Southwest, statewide Colorado and Florida, American South, first-ever Oceania entry (New Zealand: Auckland, Wellington, Christchurch, Queenstown) plus South Australia, Saudi Arabia (Riyadh, Jeddah), expanded Türkiye (Cappadocia), and countrywide Poland and Czechia |
| The World's 50 Best Restaurants | Global list + regional spinoffs | `theworlds50best.com/list/1-50` for the global list; regional lists under the same domain (exact sub-paths unverified) | Site itself is the index | Free, no paywall | World's 50 Best Restaurants 2026 ceremony is in Lima, Peru, Nov 2026 (first South America host). Asia's 50 Best Restaurants 2026 was revealed Mar 2026 in Hong Kong (No. 1: The Chairman). Latin America's 50 Best Restaurants 2026 ceremony is Dec 2026 in Guadalajara |
| The World's 50 Best Bars | Global + Asia's 50 Best Bars | Same domain family | Same | Free | Asia's 50 Best Bars 2026 revealed Jul 2026 in Macau (No. 1: Hope & Sesame, Guangzhou). There is no standalone "Latin America's 50 Best Bars"; that region is folded into North America's 50 Best Bars (which also covers Mexico and the Caribbean) |
| Monocle | Monocle Travel Guide Series (books) and "The Monocle Guide to..." | Published by Gestalten; newer "Handbook" spinoff (e.g. *Thailand: The Monocle Handbook*, 6th installment, spring 2026) is via Thames & Hudson | n/a (print/book product) | Books are a paid product | Digital city guides on monocle.com: roughly 23 cities live as of early 2026, with a stated target of 50 by end of 2026 (Palma was the 23rd; Abu Dhabi, Seoul, Amsterdam, Dubai, Sydney in progress) |
| Monocle | Digital city guides on monocle.com | `monocle.com` city guide pages | n/a | Hard paywall: Digital tier roughly $130/yr, Print+Digital roughly $260/yr, Premium $450+/yr | Effectively inaccessible without a subscription |
| Wallpaper* | City guides (architecture/design bias) | `wallpaper.com/travel/[city]` (unverified pattern, not fetch-confirmed) | n/a | Metered paywall, roughly $8.99/mo via Wallpaper*/Apple News+ | Relaunched print "Travel Guides" (formerly City Guides) in 2026 covering London, Milan, Paris, New York, sold separately |
| Financial Times | HTSI (formerly "How to Spend It") | Under `ft.com`, HTSI section | n/a | Hard/metered paywall | Rebranded from "How to Spend It" to HTSI in May 2022; still the current name in 2026, editor Jo Ellison |
| Financial Times | FT Globetrotter | `ft.com/globetrotter` | Section front page lists covered cities | Hard/metered paywall (same as main FT) | Confirmed still active in 2026 (a real risk item worth re-checking; do not assume from memory). Reported city roster (London, Paris, Rome, Madrid, Milan, Frankfurt, Zurich, Copenhagen, Venice, Edinburgh, New York, Miami, Toronto, Vancouver, Tokyo, Hong Kong, Singapore, Mumbai, Melbourne, Lagos) is plausible but not independently fetch-verified, treat the exact list as indicative |
| Bloomberg | Pursuits, recurring "Five Top Tables" city-dining column | `bloomberg.com/pursuits` | n/a | Hard/metered paywall, roughly $40/mo | Confirmed active in 2026. Specific article slugs returned by search tools should be treated as unverified rather than assumed real |
| The Infatuation | City restaurant guides | `theinfatuation.com/[city]` (unverified pattern, not fetch-confirmed) | n/a | Free | Owned by JPMorgan Chase since Sept 2021, feeding Chase Sapphire "Exclusive Tables." Covers 50+ cities in 2026: major US markets plus London, Paris, Rome, Amalfi Coast, Madrid, Barcelona, Tokyo, Melbourne, Sydney, Hong Kong, Mexico City, Accra. Zagat (acquired from Google 2018) is a distinct sub-brand under the same ownership |
| Time Out | \<City\> "best of" lists | `timeout.com/[city]` (unverified pattern, not fetch-confirmed) | n/a | Free | Print mostly discontinued (London flagship ended print June 2022; Barcelona and Madrid went digital-only by 2024). Owned by Time Out Group PLC, largest shareholders Oakley Capital and Lombard Odier. Claims roughly 108 cities across 39 countries in 2026, though the company's primary revenue driver has shifted to Time Out Market food halls rather than editorial |

### 1.2 Traditional guidebooks and general travel lifestyle media

| Publisher / owner | What it covers | URL pattern (real example) | Paywall | 2026 notes |
|---|---|---|---|---|
| Lonely Planet, owned by Red Ventures (also owns CNET, NerdWallet, The Points Guy) since Dec 2020 | Destination guides, itineraries, articles | `lonelyplanet.com/usa/new-york-city`; articles at `/articles/[slug]` | Free editorial; guidebooks/app are paid | Launched "Lonely Planet Journeys" (bookable local-expert itineraries, fall 2025) and a new app with an AI trip-planning assistant (March 2026) |
| Rough Guides, owned by Apa Digital AG (Apa Group, Switzerland), same parent as Insight Guides | Destination guides, itineraries, "things not to miss" lists | `roughguides.com/usa/new-york-city/`, sub-pages e.g. `/things-not-to-miss/` | Free online; free eBook bundled with print purchase since 2019 | Positions itself as a "travel tech company," monetizing via guidebook sales and a "tailor-made trips" booking service |
| Fodor's, owned by Internet Brands (a KKR portfolio company) since 2016 | City/region guides, sights/restaurants/hotels counts, itineraries | `fodors.com/world/north-america/usa/new-york/new-york-city` | Free, ad-supported | Annual Go List / No List still running: 2026 edition (26 "go" destinations, 8 "no" overtourism-risk destinations) published Nov 2025 |
| Frommer's, FrommerMedia LLC, family-owned, led by Editorial Director Pauline Frommer | Destination guides, "Best of" lists, itineraries, guidebooks | `frommers.com/destinations/new-york-city`, sub-pages `/planning-a-trip`, `/best-of` | Free online; guidebooks are the paid product | Still actively publishing in 2026 (2026-edition guidebooks for NYC, Paris, Italy, Ireland). Founder Arthur Frommer died in late 2024; brand continues under his daughter |
| Atlas Obscura, independent (reported its first profitable year in 2025) | Per-city "obscure sites" listicle pages and individual place pages | City hub `atlasobscura.com/things-to-do/new-york-city`; individual entries at `/places/[slug]` | Free, no paywall | No longer runs its own tours directly; "Atlas Obscura Adventures" trips are now operated in partnership with Intrepid Travel. Also the sole named "Travel Expert" content partner for Apple Maps |
| Culture Trip, acquired by U.S. News & World Report in Feb 2024 | Destination "things to do / eat & drink / places to stay" hub pages, articles | `theculturetrip.com` hub pages (exact slug unverified in this pass) | Free editorial; revenue increasingly from bookings, not ads | Major scale reduction confirmed: 2023 layoffs and management buyout from PPF Group, then sold to U.S. News in 2024. Editorial output shifted from high-volume SEO articles toward a "content-to-commerce" model built around direct trip bookings and affiliate commissions. Treat exact current headcount/revenue figures as unverified |
| Afar, independent (AFAR LLC, a public benefit company) | City/region travel guides, magazine features | `afar.com/travel-guides/united-states/new-york/new-york-city` | Hybrid: most web articles free; full magazine features/archive gated behind a roughly $8.99/mo digital subscription | No major 2026 ownership change found; unusual among peers in remaining independently operated |
| Travel + Leisure, Dotdash Meredith (IAC) | City/region guides, hotel/airline/destination rankings | `travelandleisure.com/travel-guide/new-york-city` | Free editorial, ad-supported | Annual World's Best Awards confirmed still running: 2026 edition (31st annual) announced Jul 2026, based on 207,000+ reader survey responses, paired with an industry "World's Best Summit" |
| Saveur, independent since April 2023 under Editor-in-Chief/CEO Kat Craddock, previously owned by Recurrent Ventures and originally Bonnier | Food-forward travel content, "Eat Like a Local" city guides | `saveur.com/travel/` | Likely a metered paywall on digital content; exact free-article limits unverified | Multiple ownership changes: Bonnier to Recurrent Ventures/North Equity (print paused) to independent under Craddock (print relaunched biannually) |
| Bon Appetit, Conde Nast | City dining guides (e.g. annual "Best New Restaurants"), recipe/food content | `bonappetit.com/story/best-new-restaurants-[year]` | Metered paywall; digital subscription roughly $20.99/yr, often bundled with Epicurious at roughly $30/yr | Epicurious functions as Conde Nast's food-content aggregation/app layer (Bon Appetit + Epicurious + Gourmet archive) rather than a separate acquisition of Bon Appetit itself |

### 1.3 Architecture-specific sources

| Source | What it is | URL pattern (real example) | Paywall | Notes |
|---|---|---|---|---|
| ArchDaily | Global architecture publication with both a structured project database and curated city-guide editorial | Country search `archdaily.com/search/projects/country/[country-slug]`; city search `.../search/projects/city/[city-slug]`; editorial guides `archdaily.com/[id]/[city]-architecture-city-guide` (confirmed real examples for Rome, Vancouver, Copenhagen); index at `archdaily.com/category/city-guides` or tag `archdaily.com/tag/city-guide` | Free | Search filters are UI-driven and not always deep-linkable beyond the base slug |
| Dezeen | Design/architecture news, ad hoc "guide" long-reads rather than a systematic city series | Tag page `dezeen.com/tag/architecture-guides/` | Free | Weaker fit for systematic per-city coverage than ArchDaily; better for thematic/event-driven content (design weeks, expos, landmark openings) |
| Architectural Digest, Conde Nast | Recurring "AD City Guide" travel features and an "Emerging Luxury Cities" series | Likely pattern `architecturaldigest.com/story/ad-city-guide-[city]` or a gallery variant (unverified, no live citation found; confirm before relying on it) | Metered paywall (Conde Nast) | Exact slug unconfirmed, spot-check before publishing to end users |
| Open House Worldwide network | Federation of roughly 60 independently run "Architecture Weekend" festivals: normally closed buildings opened free for one weekend a year with expert-led tours | Network hub `openhouseworldwide.org` lists all member cities; local chapters use their own domains, e.g. London `open-city.org.uk`, New York `ohny.org`, Chicago `architecture.org/openhousechicago` | Free (some ticketed premium tours) | Roughly 60 cities across 6 continents as of 2026, including London, New York, Chicago, Barcelona, Madrid, Milan, Rome, Naples, Santiago, Mexico City, Seoul, Melbourne, Istanbul. No unified URL scheme, resolve via the worldwide directory first |
| Docomomo International | Committee for documentation and conservation of Modern Movement buildings; ~80 national/regional chapters, each with its own register | Main portal `docomomo.com`; chapter directory `docomomo.com/chapters/`; US register example `docomomo-us.org/explore-modern` (filterable by state/city/status) | Free, public | No single cross-country register exists; the cross-country "MoMove" map tool was reported under maintenance in 2026. Route through the chapter directory rather than assuming one canonical URL pattern |
| UNESCO World Heritage List | Official UN heritage-sites list | Browse by country: `whc.unesco.org/en/statesparties/[country-code]` (e.g. `/jp` for Japan, `/it` for Italy); full list at `whc.unesco.org/en/list/` | Free, fully public | As of the July 2026 committee session: 1,273 sites across 173 countries, 196 States Parties total |

### 1.4 Craft and artisan sources

| Source | What it is | URL / example | Paywall | Notes |
|---|---|---|---|---|
| Kogei Japan (reference model) | Official English-language, METI-backed directory of Japan's roughly 244 nationally designated traditional crafts, by region and category | `kogeijapan.com` (English portal at `kogeijapan.com/locale/en_US/`) | Free | Gold-standard model: government-backed, bilingual, searchable by prefecture and craft type. Other countries only partly match this |
| UK, Crafts Council | National charity promoting British craft; maker directory and the Collect fair | Directory `craftscouncil.org.uk/directory`; permanent collection `collections.craftscouncil.org.uk` | Free | Print *Crafts* magazine closed in 2024, replaced by digital resources and a biannual Makers Survey. Runs the "Collect" contemporary craft fair annually at Somerset House, London |
| France, Ateliers d'Art de France | National trade body for roughly 6,000 French artisans (ceramics, jewelry, cabinetmaking, etc.) | Directory under `ateliersdart.com` (annuaire/répertoire section); events `ateliersdart.com/actualites-evenements` | Free | Runs the International Heritage Fair (Carrousel du Louvre) and the Journées Européennes des Métiers d'Art (JEMA) annually |
| South Korea, Korea Craft & Design Foundation (KCDF) | Public institution under the Ministry of Culture, Sports and Tourism; the national craft/design promotion agency | `kcdf.or.kr` (English section) | Free | Closest non-Japanese functional equivalent to Kogei Japan. Runs KCDF Gallery in Insadong, Seoul, plus Korea Craft Week |
| Italy, Fondazione Cologni dei Mestieri d'Arte + Well-Made | Foundation for Italian artisan heritage and apprenticeship training, plus a curated artisan directory | `fondazionecologni.it`; directory `well-made.it`; also partners in the international Homo Faber biennial (`homofaber.com`) | Free | No single Italian artisan-guild registry like Kogei Japan exists; these two together form the closest equivalent |
| Wallpaper* craft coverage | Ongoing craft journalism: artisan profiles, craft-fair coverage, prize coverage | No stable `/craft` tag confirmed; articles sit under `/design/` or `/lifestyle/` with craft-related slugs | Free (standard Wallpaper* access) | Treat as an editorial feed to mine, not a structured directory |
| Loewe Craft Prize | Annual EUR 50,000 international craft prize (LOEWE Foundation), shortlisting roughly 30 artisans a year from 100+ countries | `loewecraftprize.com`, redirects to `craftprize.loewe.com` | Free to browse | 2026 shortlist spanned 19 countries (Korea, Japan, Ghana, Italy, US, UK, Nigeria, Zimbabwe among others). Useful as a rotating index of top global artisans, tagged by country and discipline |

### 1.5 Menswear, heritage retail, and shop-guide sources

| Source | Coverage | URL / example | Paywall | Notes |
|---|---|---|---|---|
| Heddels | Raw denim, heritage workwear, buying guides, history | Store guide section `heddels.com/profiles/store-profiles/` (not a clean per-city index); dated posts at `/YYYY/MM/[slug]/` | Free | Monetized via newsletter, affiliate links, and its own shop |
| Put This On | Classic menswear commentary and buying advice | Standard post URLs, no city-guide format | Core editorial free; a separate weekly "Inside Track" feature is gated behind a paid membership tier (unverified exact price, roughly $5/mo per secondary sources) | Confirmed still actively posting in 2026 |
| No Man Walks Alone | Product/lookbook editorial, maker spotlights, occasional travel-adjacent diary posts | `nomanwalksalone.com/blogs/newsroom` (not `/blogs/journal`) | Free | Not a shop-guide resource, do not use for "shops in city" queries |
| Permanent Style (Simon Crompton) | City shopping guides for menswear, tailoring, and heritage retail | Hub page `permanentstyle.com/the-city-shopping-guide`; individual guides follow a dated pattern, e.g. `permanentstyle.com/2024/05/paris-a-menswear-shopping-guide-2024-update.html` (pattern confirmed via the live hub link, individual slugs not independently fetched) | Core shopping-guide articles free; a separate paid Permanent Style Magazine and Reader's Area also exist | Covers London, Paris, Tokyo, Naples, Rome, Hong Kong, Milan, Florence, New York, among others, and is periodically updated |
| Die Workwear | Classic menswear blog with cultural/historical framing | No dedicated shop/city-guide format; sidebar links and seasonal sales roundups instead | Free | Not structured as a city guide |
| Hypebeast / Highsnobiety | Streetwear and sneaker culture, including "best sneaker shops in \<city\>" posts | Standard editorial posts, no distinct URL namespace confirmed | Free, ad-supported | Highsnobiety reportedly exited third-party e-commerce in late 2025 to refocus on editorial and agency work (unverified detail); does not affect guide availability |
| Selectism | Formerly an independent streetwear/shop-crawl site | n/a | n/a | Confirmed absorbed into Highsnobiety in 2015; no longer a standalone source, remove from active rotation |

### 1.6 Coffee

| Source | Coverage | URL / example | Paywall | Notes |
|---|---|---|---|---|
| Sprudge | US-leaning global coffee-culture site with dated city guides | Index at `sprudge.com/guides`; individual posts dated, e.g. "The Sprudge Guide To Coffee In Chicago" | Free | Direct fetch blocked by a local CA-cert issue in research; existence and pattern confirmed via search-grounded citations |
| European Coffee Trip | Europe-specific city and country coffee-shop guides plus a companion app | `europeancoffeetrip.com` | Free web guides; app has free and possibly premium tiers (unverified) | Claimed coverage of 39 countries and 6,000+ cafes, treat exact figures as unverified |

### 1.7 Photography-specific resources

| Resource | What it does | Notes |
|---|---|---|
| Capture the Atlas | Travel-photography site with per-city/region "best photo spots" guides | Established, real publication; granular spot lists should be spot-checked at build time since they can go stale |
| SunCalc (`suncalc.org`) | Free browser-based sun-position, golden-hour, blue-hour, and shadow-length calculator | Long-established and widely cited, works for any coordinate worldwide |
| PhotoPills | Paid all-in-one planning app: sun/moon/Milky Way alignment, AR view, shadow and depth-of-field calculators | Real, confirmed; exact current pricing unverified |
| Instagram geotags / Flickr geo-search | Searching a location's geotag feed on Instagram, or Flickr's map-based "interesting near X" search, to discover photogenic viewpoints | A technique, not a stable URL. Instagram location pages follow `instagram.com/explore/locations/[id]/`, but the numeric IDs are not human-guessable and should not be presented as a lookup pattern |

### 1.8 Cycling

| Resource | What it covers | URL pattern | Paywall | Notes |
|---|---|---|---|---|
| bikepacking.com | Original and curated bikepacking routes in 70+ countries, GPX files, logistics | `bikepacking.com/routes/location/[region]/[country]/` | Core route database free; paid "Bikepacking Collective" membership (roughly $68/yr) unlocks community tools only | Route content itself stays free even without membership |
| komoot | "Highlights" (community POIs) and "Collections" (curated route sets) | Tour `komoot.com/tour/[ID]`; collection `komoot.com/collection/[ID]`; region discovery `komoot.com/discover/[region]` | Browsing free; full route planning (multi-day, offline maps, device sync) requires Premium (roughly $59.99/yr) since a Feb 2025 policy change following the Bending Spoons acquisition | Legacy pre-2025 users retain a one-time-purchase option; new users do not |
| EuroVelo | 17-route EU-backed long-distance cycle network | By route `eurovelo.com/en/eurovelos/eurovelo-[number]`; by country `eurovelo.com/en/[country]`; planner at `eurovelo.com/en/route-planner` | Free | Europe-specific |
| National cycle networks | Country-level route authorities | UK: National Cycle Network via `sustrans.org.uk` / `walkwheelcycletrust.org.uk` (Sustrans legally renamed itself Walk Wheel Cycle Trust in Aug 2025, same charity, same remit). US: Adventure Cycling Association, `adventurecycling.org/routes-and-maps`, 50,000+ miles plus the U.S. Bicycle Route System | Free | Other countries (Netherlands, Germany, etc.) likely have equivalent bodies (unverified in this pass); search for the national cycling federation |
| Strava Global Heatmap | Aggregated public GPS activity showing where people ride/run/swim most, rolling roughly 12 to 13 months | `strava.com/heatmap` | The Global Heatmap itself is free; paid subscription (roughly $11.99/mo) unlocks Personal, Weekly, and Night heatmap variants plus route-builder integration | Useful for finding locally popular routes when traveling |

### 1.9 Hiking and outdoors

| Resource | Coverage | URL pattern | Paywall | Notes |
|---|---|---|---|---|
| AllTrails | Roughly 550,000+ trail database worldwide | Country `alltrails.com/[country]`; region/state `alltrails.com/[country]/[state]`; city `alltrails.com/[country]/[state]/[city]`; trail `alltrails.com/trail/[country]/[state]/[trail-name]` | Freemium: base tier free; paid AllTrails+ (roughly $35.99/yr) or the higher AllTrails Peak tier (roughly $79.99/yr) gate offline maps, real-time alerts, live location sharing, and device sync | Rebranded from a single "Pro" tier into the Plus/Peak structure recently, flag if referencing older material |
| National park authorities | Real-time closures and trail conditions | US example: `nps.gov/[4-letter-code]/planyourvisit/conditions.htm`; UK example: `peakdistrict.gov.uk`, `lakedistrict.gov.uk`, portal at `nationalparks.uk` | Free, public | Authoritative over crowdsourced apps for closures since it reflects agency data directly |
| AllTrails alternatives | Komoot (also used for hiking, not just cycling), Wikiloc (strong in Spain and Latin America), Outdooractive (strong in the DACH region: Germany, Austria, Switzerland) | Komoot `komoot.com/guide/[ID]/hikes-in-[region]`; Wikiloc `wikiloc.com/hiking-trails/[country]/[region]`; Outdooractive `outdooractive.com/en/travel-guide/[region-name]` | Freemium, varies by platform | Also worth knowing: Gaia GPS (technical backcountry), FarOut (thru-hiking guides), Mapy.cz (free European offline maps) |

### 1.10 Local-language sources worth machine-translating

| Source | Country / focus | URL | Notes |
|---|---|---|---|
| Tabelog | Japan restaurant reviews | `tabelog.com` | Notoriously strict rating scale; 3.5/5 is considered excellent, only roughly 3 percent of listings exceed it |
| Dianping (大众点评) | China restaurant and local-life reviews plus bookings | `dianping.com` | Roughly 150M monthly active users |
| Naver Map | Korea's dominant local search and navigation tool | `map.naver.com` | Distinguishes receipt-verified "visitor reviews" from promotional "blog reviews"; reintroduced star ratings in April 2026 after a 5-year hiatus |
| Il Gambero Rosso | Italy restaurant and wine guide | `gamberorosso.it` | Publishes annual Ristoranti d'Italia and Vini d'Italia guides; also runs a "Top Italian Restaurants Abroad" tour |
| Guia Repsol | Spain (plus Portugal) restaurant guide | `guiarepsol.com` | Uses a "Soles" (Suns) rating system, positioned as a Michelin competitor |
| Le Fooding | France (plus Belgium) guide | `lefooding.com` | Favors independent, neighborhood spots over fine dining |
| Gault&Millau | Multi-country: separate national editions for France, Austria, Germany, Switzerland, Italy, Japan and others | `gaultmillau.com` plus country-specific domains | 2026 expansion added China and the Baltic states |
| Falstaff | Austria/Germany food and wine guide | `falstaff.com` | Core coverage is Austria, Germany, Switzerland, with added Nordic-region guides |
| Foursquare City Guide | Formerly a consumer city-guide app | n/a | Fully shut down: mobile app in Dec 2024, web in April 2025. It no longer exists as a consumer product. Swarm remains the only active consumer app (check-ins and lists); Foursquare itself pivoted to B2B geospatial data licensing. Remove from active rotation as a travel-planning source |
| OpenRice | Hong Kong (also Taiwan and mainland China secondary markets), restaurant reviews and bookings | `openrice.com` | Long-established, widely used regional equivalent of Yelp for Greater China dining; the default local-language cross-check for Hong Kong |
| Zomato | India, and several Middle East and Southeast Asia markets, restaurant discovery and delivery | `zomato.com` | Dominant in India specifically; review quality skews more toward delivery-order reviews than in-person dining reviews in some markets |
| Kakao Map | Korea, alternative to Naver Map with a different user base and review mix | `map.kakao.com` | Worth checking alongside Naver Map rather than instead of it, since the two platforms' user bases do not fully overlap |
| Yandex Maps | Russia and several ex-Soviet markets, local search and reviews | `yandex.com/maps` | The dominant local mapping and review platform in markets where Google Maps has reduced functionality or reduced local review density |
| Google Maps reviews | Universal fallback everywhere Google Maps operates | `google.com/maps` | Review density and recency vary enormously by country; the floor-level check everywhere, not a substitute for a stronger local-language platform where one exists |
| HappyCow | Global vegan and vegetarian restaurant directory | `happycow.net` | Useful as a category-specific overlay on top of general local-language platforms for travelers with dietary restrictions, in any country |
| TripAdvisor | Global reviews and forums | `tripadvisor.com` | Useful as a floor-level source for smaller destinations with thin editorial coverage (see 1.12), but more exposed than most sources here to fake or incentivized reviews; corroborate rather than rely on alone |

### 1.11 Reddit and forum sources

- Country and city subreddits generally follow `r/[CountryOrCity]` or `r/[Country]Travel` (e.g. r/JapanTravel, r/london, r/AskAFrench). Many have a paired tourist-specific companion sub the community redirects casual questions to (e.g. r/london points visitors to r/VisitLondon; r/JapanTravel points to r/JapanTravelTips). Search via a general web search engine with `site:reddit.com r/[sub] [query]`, or Reddit's own in-subreddit search.
- Many travel subreddits now actively moderate against AI-generated itinerary posts, worth keeping in mind when citing a subreddit as a "human-verified" source.
- Chowhound: the original discussion forums shut down (commonly cited around 2022, though some sources say later; treat the exact year as unverified). The brand itself was separately relaunched by Static Media in Nov 2023 as an editorial recipe site with no forums, so "Chowhound" today is not the community resource it once was. Real successor communities exist: Hungry Onion (Discourse-based, founded by a former Chowhound user, generally considered the closest spiritual successor) and Food Talk Central (West Coast and LA-focused). Reddit food subreddits (r/Cooking, r/AskCulinary, city-specific food subs) have absorbed much of the remaining traffic.
- Hacker-News-style local city forums are highly city-dependent and no universal directory exists. Check for a dedicated city subreddit first, then search generically for "\<city\> forum" or "\<city\> Discourse community" rather than assuming a specific niche forum exists.

---

## 2. Paywall access playbook

Prefer legitimate access wherever it exists. Only fall back to bypass techniques when no legitimate option is available, and treat every bypass technique as unreliable enough to need a fallback plan.

| Technique | How it works | Reliability in 2026 | Notes |
|---|---|---|---|
| **removepaywalls.com to accessarticlenow.com (PRIMARY, verified)** | `removepaywalls.com/<FULL-URL>` renders the article inside an iframe whose src is `https://accessarticlenow.com/api/c/full?q=<FULL-URL>`. **Navigate a browser-automation agent directly to that accessarticlenow URL.** Reaching into the iframe does not work: `frame "iframe"` returns "Frame not found", and `frame @<ref>` attaches but frame context resets between CLI invocations, so the next `eval` runs against the outer document and returns about 160 characters of chrome. | **High, and empirically verified.** Confirmed working across 27 Conde Nast Traveler articles in the July 2026 Japan build, about 2.7 MB of harvested text. The direct-URL navigation turned 163 characters into 5,338 characters of article text on the first test. | This is the method the user supplied and it is the default. The `/api/c/full?q=` path is confirmed by direct use, not inference; disregard secondary sources describing an `/api/c/js?q=` variant. If the shape ever changes, re-derive it rather than guessing: open the removepaywalls URL, `agent-browser snapshot -i`, then `agent-browser get attr <iframe-ref> src`. |
| archive.today (archive.ph, .md, .is, .li mirrors) | Submit a live URL to force a fresh crawl and snapshot ("red box"), or search existing snapshots by exact URL, domain (`insite:`), or wildcard ("black box"). Ignores robots.txt, so it can capture pages the Wayback Machine cannot. | Mixed and unstable. Multiple monitoring reports showed archive.ph and archive.today reporting down in mid-August 2026 while archive.is stayed up; a broader multi-domain outage was reported in June 2026. When a mirror works: New York Times success rate is rated high, Wall Street Journal moderate (strip tracking parameters before submitting), Financial Times low to moderate (roughly 50 to 60 percent success spoofing a Googlebot user agent). | If one mirror is down, try the others (.ph, .md, .is, .li). A reported Wikipedia blacklist (Feb 2026) and regional blocking are single-sourced and unverified, but worth keeping in mind if a submission is rejected. |
| archive.org Wayback Machine | Snapshots the rendered page as crawled; does not actively strip paywalls. | Low for anything published in roughly the last 12 to 18 months on major outlets. Many major news sites (reportedly including the New York Times, the Guardian, and the USA Today network) updated robots.txt to block the Internet Archive crawler starting around August 2025, largely over AI-scraping concerns. Metered paywalls also mean the crawler often captures the "subscribe" block itself rather than the article text. | Better suited to older articles (pre-2024/2025) than to recent ones. A specific claim that 241 news organizations block the crawler is single-sourced and should be treated as unverified, but the general trend is corroborated by multiple sources. |
| 12ft.io | Formerly rewrote pages using Google-cache tricks and script stripping. | Dead. Confirmed by multiple corroborating sources: the domain was taken down on July 14, 2025 after legal pressure from the News/Media Alliance. It does not resolve in 2026. | Do not include as a working technique. Community forks ("13ft", self-hosted variants) and "1ft.io" clones are mentioned in some places as replacements but are unverified and low-confidence, not something to recommend without further vetting. |
| Google Cache (`cache:` search operator, or the cached-page link) | Formerly showed Google's stored copy of a page, independent of the live page's paywall state. | Confirmed dead. Google removed the "Cached" link in Feb 2024 and fully disabled the `cache:` operator by Sept 2024. Still gone as of 2026; Google now shows Wayback Machine links in "About this result" instead. | High-confidence, multi-source consensus. Do not include as a working technique. |
| Browser reader modes (Safari Reader, Firefox Reader View, Edge immersive reader) | Strips CSS/JS overlays client-side, revealing underlying DOM text still delivered to the browser. | Works only against soft or cosmetic paywalls, an overlay covering text the browser already received. No effect on hard, server-side paywalls where the article text is never sent at all. | Fully legitimate, no terms-of-service ambiguity since it acts only on content already delivered to the user's own browser. |
| Print URLs and AMP URLs | `/print/` variants or `?outputType=amp` sometimes serve a stripped-down version with looser paywall logic. | Declining and largely unreliable in 2026. Google officially discontinued serving pages from the AMP Cache/Viewer on July 1, 2026, and most major publishers (New York Times, Vox, CNBC, among others) have already migrated off AMP entirely, so AMP URLs increasingly 404 or redirect. Print URLs are publisher-specific and undocumented. | Treat as a low-odds fallback, not a primary technique. |
| Bypass Paywalls Clean (open-source browser extension) | A community-maintained fork of an older "Bypass Paywalls" extension, installed manually (not distributed through official extension stores due to publisher takedown pressure) and targets specific known paywall implementations with per-site rules. | Works well for sites its ruleset explicitly covers, breaks whenever a publisher changes its paywall implementation, and requires the user to trust and manually install an unofficial browser extension from source rather than a store listing. | Better suited to a user's personal browser setup than to an automated agent workflow, since it needs manual installation and periodic ruleset updates; mention it as an option for a technically comfortable user rather than something to invoke programmatically. |
| Incognito or private browsing mode | Resets cookies used by metered (soft) paywalls to count how many free articles a reader has used this month. | Works only on cookie-based metering, has no effect on hard paywalls or on server-side account-based metering tied to an IP or logged-in state. | Simple, fully legitimate, and often the first thing worth trying on a metered site like the Economist before reaching for any other technique. |
| Mobile app vs. mobile web asymmetry | Some publishers enforce a paywall inconsistently between their app and their mobile website, or between mobile web and desktop web. | Inconsistent and publisher-specific, changes without notice, not something to rely on as a rule. | Worth a quick try (open the same URL on mobile web if only the desktop version is blocked, or vice versa) but not worth building a systematic workflow around. |
| Outline.com (historical reference only) | A now-defunct paywall-stripping tool previously owned by Evernote. | Dead, shut down in 2020. | Included here only so it is not mistakenly recommended from outdated training data or an old forum post; do not suggest it. |

**Legitimate access, prefer these first:**

- Library access to NYT: a real, widely available program. Confirmed examples: the New York Public Library announced free unlimited on-site NYT access via library Wi-Fi in Jan 2026 (a library card is only needed to reserve a public PC, not for on-site Wi-Fi access); Chicago Public Library offers 24-hour redeemable access codes; other systems (Seattle, Boston, Los Angeles, San Francisco) offer 72-hour passes. Specific dates come from library and aggregator sites rather than the New York Times itself, treat exact dates as reasonably reliable but secondary-sourced; the underlying program is well-documented and long-standing. Ask the user if they have a library card before reaching for a bypass technique.
- Personal subscriptions: unambiguous, use if the user already has one.
- Publisher free-article allowances: reported 2026 figures put the Financial Times on dynamic AI-based metering (roughly 8 articles a month for occasional readers, plus 10 to 20 subscriber gift-article credits a month), Bloomberg at roughly 1 free article a month for registered users, and the Economist on a small weekly (not monthly) metered allotment via cookies. These figures are secondary-sourced and dynamic paywalls change without notice, treat as approximate.

**The ladder, in order. Do not reorder it.**

1. **removepaywalls via the direct accessarticlenow URL.** The default for automated harvesting. This
   is the method the user supplied, it is verified at scale (27 articles), and it is the fastest
   because it needs no snapshot lookup and no submission step. Start here.
2. **archive.today** (try the .ph, .md, .is, .li mirrors in turn). Search for an existing snapshot
   first, submit the live URL if none exists. Mirrors go down intermittently.
3. **Wayback Machine.** Realistically only for articles older than roughly 2024, since many major
   outlets began blocking the crawler around August 2025.
4. **Legitimate access.** If the user has a subscription or a library card program (many US public
   libraries carry NYT), that is the highest-reliability route of all and worth asking about for a
   title that keeps failing. It is listed fourth only because it needs the user in the loop, not
   because it is worse.
5. **Stop.** Two failures on the same article, log the gap and move on. Do not loop.

**Dead, do not attempt:** 12ft.io (domain taken down July 14, 2025) and Google Cache (`cache:`
operator disabled September 2024). Both are high-confidence multi-source dead. They appear in this
document only so an agent does not burn turns rediscovering that, which is the specific failure mode
this list exists to prevent. Outline.com is also dead (2020).

---

## 3. Search patterns that surface the right articles fast

Use these as literal, adaptable templates. Replace `<city>`, `<country>`, and `<query>` with the actual target.

| Goal | Search string pattern |
|---|---|
| NYT 36 Hours coverage of a city | `site:nytimes.com "36 hours in" <city>` |
| Conde Nast Traveler restaurant picks | `site:cntraveler.com <city> restaurants` |
| Conde Nast Traveler things to do | `site:cntraveler.com <city> things to do` |
| Eater essential-restaurants map for a covered city | `site:eater.com/<city-site-slug> "essential restaurants"` (only works for cities with an active dedicated Eater site, see 1.1) |
| Eater heatmap for a city | `site:eater.com <city> heatmap` |
| Michelin-starred and Bib Gourmand listings | `site:guide.michelin.com <city>` then filter on the results page directly, since Michelin's own filter UI is more reliable than guessing a query-string filter |
| World's 50 Best mentions of a specific restaurant or city | `site:theworlds50best.com <city or restaurant name>` |
| Monocle city coverage (to check if a paywalled guide exists before deciding whether to pursue access) | `site:monocle.com <city> guide` |
| FT Globetrotter coverage of a city | `site:ft.com/globetrotter <city>` |
| The Infatuation guide check | `site:theinfatuation.com <city>` |
| Time Out best-of lists | `site:timeout.com <city> "best of"` |
| Atlas Obscura per-city obscure sites | `site:atlasobscura.com/things-to-do/<city>` |
| ArchDaily architecture guide for a city | `site:archdaily.com <city> "architecture city guide"` |
| Permanent Style shopping guide for a city | `site:permanentstyle.com <city> shopping guide` |
| Sprudge coffee guide for a city | `site:sprudge.com <city> coffee guide` |
| Local-language review site, machine-translated query | `site:tabelog.com <neighborhood>` then translate the page, rather than translating the query first (Japanese, Chinese, and Korean review sites index better on native-script neighborhood names) |
| General cross-check across several sources at once | `<city> "best restaurants" 2026` without a site filter, then manually triage which domains appear (a listicle that shows up across NYT, Eater, and a local-language source independently is a strong signal, see section 4) |
| Tag-page browsing instead of search | For any outlet with a confirmed tag/category system (ArchDaily `tag/city-guide`, Dezeen `tag/architecture-guides`, ArchDaily `category/city-guides`), browse the tag page directly rather than searching, since tag pages surface the full history including older pieces a search engine may not have indexed prominently |
| Sitemap crawling for a systematic pull | Fetch `<domain>/sitemap.xml` or `<domain>/sitemap_index.xml` and grep for the city or country slug, useful for outlets like ArchDaily or Atlas Obscura that have large, structured URL namespaces; less useful for outlets like the NYT where the sitemap is enormous and not city-segmented |
| Reddit-native search for a city subreddit | Use Reddit's own search scoped to the subreddit (`reddit.com/r/<sub>/search?q=<query>`) rather than a generic web search, since Reddit's search engine indexes comment threads that Google often misses |
| Narrowing a noisy result set by recency | Append `after:2024-01-01` (Google date-range syntax) or use the search engine's own "Tools > Any time > Custom range" filter when a city name returns mostly stale SEO content; this is especially useful for restaurant and shop queries where a 2019 listicle otherwise outranks a 2026 update |
| Finding the "best of" refresh for a recurring annual list | `<outlet> "<city>" 2026 best restaurants` (swap the year each cycle) surfaces the current edition rather than an older cached version that a plain query might return first |
| Checking whether a specific venue is still covered anywhere current | `"<venue name>" <city> 2026` with no site filter; if every hit is from 2022 or earlier, treat that as a closure-risk signal in its own right (see section 5) |

### 3.1 Ongoing monitoring rather than one-off search

For a trip being planned weeks or months in advance, or for a destination the traveler visits repeatedly, a one-off search pass goes stale. Several outlets in section 1 still expose RSS feeds even though RSS is no longer a headline feature on their sites; check for a feed at the conventional `<domain>/rss` or `<domain>/feed` path, or look for a linked feed URL in the page source, before assuming none exists. Where a feed exists, subscribing to a destination-relevant outlet's feed (or a filtered feed if the outlet supports tag-based feeds, as ArchDaily and Dezeen generally do) is a more efficient way to catch new coverage of a specific city than re-running the same search query on a schedule. Newsletter sign-ups (most Tier 1 outlets in 1.1 offer a free travel or food newsletter) are a lower-effort alternative that surfaces new coverage without needing a feed reader at all.

### 3.2 Worked example

Researching a weekend trip to Lisbon for a food-and-design-focused itinerary might run as: `site:nytimes.com "36 hours in" lisbon` to check for a Tier 1 anchor piece, `site:cntraveler.com lisbon restaurants` and `site:cntraveler.com lisbon things to do` for the Conde Nast layer, `site:archdaily.com lisbon "architecture city guide"` for the design layer, `site:timeout.com lisbon "best of"` for a broader local-best-of check, and finally a Portuguese-language check via a general search for the dominant local review platform (since Lisbon has no dedicated Eater or Infatuation site, and Guia Repsol per section 1.10 already covers Portugal alongside Spain). Cross-referencing the CNT and Time Out picks against Guia Repsol listings would catch anything that reads well in English but has thin or negative local reviews.

---

## 4. Source-quality weighting

Not all picks deserve equal trust. Use this rubric before committing a recommendation to an itinerary.

### 4.1 What makes a pick high-confidence

- Appears independently in 3 or more sources that were not obviously copying each other (a Tier 1 editorial series, a local-language review site, and a Reddit thread agreeing independently is much stronger than three English-language listicles that all cite the same original source).
- Recently published or recently updated (within the last 12 to 18 months for restaurants and shops; longer tolerances are fine for museums, monuments, and UNESCO sites, which change slowly).
- Names a specific chef, owner, or maker rather than describing the venue generically ("chef X's tasting menu" is a stronger signal than "a cozy spot known for great food").
- Comes from a source with a track record of on-the-ground reporting rather than aggregation (a Michelin inspector visit, a Sprudge staff visit, a 50 Best judging panel) rather than a site that appears to compile other outlets' lists.
- Corroborated by a receipt-verified local review platform (Tabelog, Naver Map's visitor reviews, Dianping) in addition to English-language editorial coverage.

### 4.2 What makes a pick low-confidence

- Appears in only a single listicle, especially an undated one or one clearly optimized for search-engine traffic rather than a specific visit.
- Reads as sponsored content, native advertising, or a "partner content" placement (check for disclosure language).
- Has no clear publish or update date, or the date is more than 2 to 3 years old for a fast-moving category like restaurants and shops.
- Shows obvious signs of closure risk in the underlying text itself ("was a local favorite," "used to be," reviews trailing off).
- Is the only source claiming a superlative ("the best," "the only") that no other source corroborates.

### 4.3 Rule for flagging "verify still open"

Flag any pick for a "verify still open" check before including it in a final itinerary if any of the following apply: the source is more than 12 months old for a restaurant, bar, or shop; the source is a single listicle rather than a Tier 1 recurring series; the venue is independently owned rather than part of a larger group (independents close and relocate far more often); or the city has a known high-turnover dining scene (dense, competitive urban food markets turn over faster than small towns or fixed cultural institutions).

### 4.4 Worked example

Two candidate restaurants surface for the same neighborhood: Restaurant A appears in a 2026 Michelin Bib Gourmand list, a 2025 CNT "Best Restaurants" roundup that names the chef by name, and has a cluster of Tabelog-equivalent local reviews from the last month. Restaurant B appears only in a single undated "Top 10 Hidden Gems" blog post with no named chef and generic stock-photo-style images. Restaurant A clears the high-confidence bar on every count in 4.1 and needs only a routine freshness check (5.1) before booking. Restaurant B should be treated as low-confidence per 4.2 and either dropped or, if it seems otherwise promising, escalated straight to a "verify still open" check plus a search for any independent corroboration before it goes anywhere near a draft itinerary.

### 4.5 Weighting by source tier

As a rough starting point when sources conflict, weight a pick roughly in this order, adjusting up or down based on the recency and specificity signals in 4.1 and 4.2 rather than treating this as a rigid hierarchy: a receipt-verified local-language platform review cluster, a Tier 1 recurring series with a named critic or inspector visit (Michelin, 50 Best, a byline-carrying NYT or CNT piece), a well-corroborated Reddit or forum thread from users who state they visited recently, a guidebook or general travel-media listicle, and lowest, a single undated aggregator post with no clear authorship.

---

## 5. Freshness and closure risk

### 5.1 How to check a place is still open

| Check | What it tells you | How to use it |
|---|---|---|
| Google Maps listing status | Google Maps will mark a location "Permanently closed" or "Temporarily closed" once enough signals accumulate | Search the venue by name and address, not just name, since common names collide across cities |
| Recent reviews on Tabelog, Yelp, Dianping, Naver Map, or Google | Review recency is a strong live-status signal | A cluster of reviews within the last 1 to 3 months is a good sign; a gap of 6+ months with no recent activity is a yellow flag even without a "closed" label |
| Instagram or other social account's last post date | Many small independent venues post regularly; a long silence often precedes closure | Check the account's grid or stories for a recent, location-tagged post, not just a general recent post that could be off-site |
| Reservation platform status (OpenTable, Resy, Tock, or local equivalents) | If a venue's reservation page is dead, redirects, or shows no availability far into the future, that is a signal worth investigating further | Cross-check against the venue's own site if it has one |
| Official venue website "News" or "Contact" page | Renovation notices, seasonal closure schedules, and relocation announcements are often posted here well before third-party platforms catch up | Especially useful for museums, artisan workshops, and small retail |

### 5.2 Common failure modes

- **Venue moved**: same name, new address, especially common for small restaurants and independent shops leaving a lease.
- **Chef or owner left**: the venue may still be open but no longer delivers what the original recommendation was based on; check whether a review mentions a change in kitchen leadership.
- **Renovation or refurbishment**: temporary closure that can run months longer than announced; check for a stated reopening date and treat it skeptically if it has already passed.
- **Seasonal closure**: common for beach towns, ski towns, and some artisan workshops that close for an off-season or for annual leave (many independent restaurants in parts of Europe close for 2 to 4 weeks in summer or around a national holiday).
- **Demolished or redeveloped**: most common for informal markets, pop-ups, and buildings in rapidly redeveloping neighborhoods; a UNESCO-listed or landmark building is far less exposed to this than an unlisted structure.
- **Acquired and rebranded**: the physical space and sometimes the staff persist, but the name, concept, and menu change entirely; a stale recommendation can send a traveler to a venue that no longer resembles the one being recommended.
- **Delisted rather than closed**: some venues stop appearing in an editorial series (dropped from a "best of" refresh) without actually closing; treat delisting as a signal to re-verify quality, not necessarily existence.

### 5.3 General rule

Treat any pick more than 12 months old as needing a live-status check before inclusion in a final itinerary, and treat any pick more than 24 months old as needing both a live-status check and a quality re-check (the original reason it was recommended may no longer hold even if the doors are still open).

### 5.4 Category-specific closure-risk patterns

- **Restaurants and bars**: highest turnover of any category in this catalog, especially independent, chef-driven, or trend-dependent venues in dense competitive dining markets. Group-owned or hotel-attached restaurants tend to be more stable than standalone independents.
- **Shops and retail (menswear, artisan, craft)**: moderate turnover; heritage and family-owned shops (the kind Permanent Style and Heddels tend to cover) are typically far more durable than trend-driven streetwear retail, but lease non-renewals and rent increases can close even long-running shops with little warning.
- **Museums, galleries, and cultural institutions**: low turnover but subject to long, sometimes multi-year renovation closures; always check the institution's own site for a stated reopening date rather than assuming a general "temporarily closed" flag means a short closure.
- **UNESCO World Heritage sites and government-designated landmarks**: lowest closure risk in this catalog, though individual access points, visitor centers, or specific wings can close for restoration, conservation work, or, in some cases, political or safety reasons; check the site's official visitor information rather than relying solely on the UNESCO listing itself, since UNESCO status describes designation, not current visitor access.
- **Cycling and hiking routes**: risk here is environmental and seasonal rather than commercial: landslides, wildfire closures, snowpack, and trail erosion repairs can close a route with no notice on a crowdsourced app; always cross-check against the official park or land-management authority (section 1.9) rather than relying solely on AllTrails, Komoot, or Wikiloc user reports.
- **Coffee shops**: turnover is closer to restaurants than to retail, particularly for single-location independents; a Sprudge or European Coffee Trip guide more than a year old should be treated with the same skepticism as an equally old restaurant pick.

### 5.5 Regional patterns worth knowing

Closure and turnover risk is not evenly distributed by geography either. Dense, highly competitive, high-rent dining markets (major global cities generally) tend to see faster turnover than smaller cities or towns. Some countries have a cultural pattern of long-lived, multi-generation family businesses (many small restaurants and craft workshops in Japan and parts of continental Europe, for instance) that are comparatively low risk once established. Markets with rapid real-estate development cycles, including many fast-growing Gulf and Southeast Asian cities, can see even well-regarded venues open and close within a couple of years as buildings are redeveloped. None of this should be treated as a fixed rule for any specific venue, it is a prior to adjust confidence by, not a substitute for the live-status checks in 5.1.

---

## 6. Quick-reference index

Every named source in this catalog in one scannable table, for fast lookup when building tooling or a checklist. "Section" points back to the detailed entry. "Default tier" is a starting-point confidence weighting per section 4.5, not a substitute for checking recency and specificity on the actual pick.

| Source | Category | Section | Access | Default tier |
|---|---|---|---|---|
| NYT "36 Hours in \<City\>" | Recurring series | 1.1 | Metered/hard paywall | Tier 1 anchor |
| NYT "52 Places to Go" | Recurring series | 1.1 | Metered/hard paywall | Tier 1 anchor |
| NYT restaurant reviews | Recurring series | 1.1 | Metered/hard paywall | Tier 1 anchor |
| Conde Nast Traveler city guides | Recurring series | 1.1 | Metered paywall | Tier 1 anchor |
| Conde Nast Traveler best restaurants/things to do | Recurring series | 1.1 | Metered paywall | Tier 1 anchor |
| Conde Nast Traveler Gold List | Recurring series | 1.1 | Metered paywall | Tier 1 anchor |
| Eater city maps and heatmaps | Recurring series | 1.1 | Free | Tier 1 anchor (only in active cities) |
| Michelin Guide | Recurring series | 1.1 | Free to browse | Tier 1 anchor |
| The World's 50 Best Restaurants + regional lists | Recurring series | 1.1 | Free | Tier 1 anchor |
| The World's 50 Best Bars + Asia's 50 Best Bars | Recurring series | 1.1 | Free | Tier 1 anchor |
| Monocle Travel Guide Series (books) | Recurring series | 1.1 | Paid book | Tier 1 anchor |
| Monocle digital city guides | Recurring series | 1.1 | Hard paywall | Tier 1 anchor |
| Wallpaper* city guides | Recurring series | 1.1 | Metered paywall | Category specialist |
| FT HTSI | Recurring series | 1.1 | Hard/metered paywall | Tier 1 anchor |
| FT Globetrotter | Recurring series | 1.1 | Hard/metered paywall | Tier 1 anchor |
| Bloomberg Pursuits | Recurring series | 1.1 | Hard/metered paywall | Tier 1 anchor |
| The Infatuation | Recurring series | 1.1 | Free | Tier 1 anchor (only in covered cities) |
| Time Out \<city\> | Recurring series | 1.1 | Free | Guidebook-equivalent |
| Lonely Planet | Guidebook | 1.2 | Free editorial, paid guidebooks/app | Guidebook-equivalent |
| Rough Guides | Guidebook | 1.2 | Free editorial, paid guidebooks | Guidebook-equivalent |
| Fodor's | Guidebook | 1.2 | Free | Guidebook-equivalent |
| Frommer's | Guidebook | 1.2 | Free editorial, paid guidebooks | Guidebook-equivalent |
| Atlas Obscura | Guidebook | 1.2 | Free | Category specialist (obscure sites) |
| Culture Trip | Guidebook | 1.2 | Free | Guidebook-equivalent (verify currency, reduced staff) |
| Afar | Guidebook | 1.2 | Hybrid: free web, paid magazine archive | Guidebook-equivalent |
| Travel + Leisure | Guidebook | 1.2 | Free | Guidebook-equivalent |
| Saveur | Guidebook | 1.2 | Likely metered (unverified specifics) | Category specialist (food) |
| Bon Appetit | Guidebook | 1.2 | Metered paywall | Category specialist (food) |
| ArchDaily | Architecture | 1.3 | Free | Category specialist |
| Dezeen | Architecture | 1.3 | Free | Category specialist |
| Architectural Digest travel | Architecture | 1.3 | Metered paywall | Category specialist |
| Open House Worldwide network | Architecture | 1.3 | Free (some ticketed tours) | Category specialist |
| Docomomo International | Architecture | 1.3 | Free | Category specialist |
| UNESCO World Heritage List | Architecture | 1.3 | Free, public | Tier 1 anchor (for heritage sites specifically) |
| Kogei Japan | Craft | 1.4 | Free | Category specialist |
| UK Crafts Council | Craft | 1.4 | Free | Category specialist |
| France Ateliers d'Art de France | Craft | 1.4 | Free | Category specialist |
| Korea KCDF | Craft | 1.4 | Free | Category specialist |
| Italy Fondazione Cologni / Well-Made | Craft | 1.4 | Free | Category specialist |
| Wallpaper* craft coverage | Craft | 1.4 | Free | Category specialist |
| Loewe Craft Prize | Craft | 1.4 | Free to browse | Category specialist |
| Heddels | Menswear/retail | 1.5 | Free | Category specialist |
| Put This On | Menswear/retail | 1.5 | Free core, paid membership tier | Category specialist |
| No Man Walks Alone journal | Menswear/retail | 1.5 | Free | Not a shop-guide source, low utility for this use |
| Permanent Style shop guides | Menswear/retail | 1.5 | Free | Category specialist |
| Die Workwear | Menswear/retail | 1.5 | Free | Not a shop-guide source, low utility for this use |
| Hypebeast / Highsnobiety | Menswear/retail | 1.5 | Free | Category specialist |
| Selectism | Menswear/retail | 1.5 | n/a (absorbed into Highsnobiety) | Defunct, do not use |
| Sprudge | Coffee | 1.6 | Free | Category specialist |
| European Coffee Trip | Coffee | 1.6 | Free web | Category specialist |
| Capture the Atlas | Photography | 1.7 | Free | Category specialist |
| SunCalc | Photography | 1.7 | Free | Category specialist (tool, not editorial) |
| PhotoPills | Photography | 1.7 | Paid app | Category specialist (tool, not editorial) |
| Instagram/Flickr geo-search | Photography | 1.7 | Free | Community, verify recency |
| bikepacking.com | Cycling | 1.8 | Free routes | Category specialist |
| komoot | Cycling/hiking | 1.8, 1.9 | Freemium | Category specialist |
| EuroVelo | Cycling | 1.8 | Free | Category specialist (Europe only) |
| National cycle networks | Cycling | 1.8 | Free | Category specialist |
| Strava Global Heatmap | Cycling | 1.8 | Free (paid variants) | Community signal, not editorial |
| AllTrails | Hiking | 1.9 | Freemium | Category specialist |
| National park authorities | Hiking | 1.9 | Free, public | Tier 1 anchor (for conditions/closures) |
| Wikiloc | Hiking | 1.9 | Freemium | Category specialist |
| Outdooractive | Hiking | 1.9 | Freemium | Category specialist |
| Tabelog | Local-language | 1.10 | Free | Local-language anchor (Japan) |
| Dianping | Local-language | 1.10 | Free | Local-language anchor (China) |
| Naver Map | Local-language | 1.10 | Free | Local-language anchor (Korea) |
| Il Gambero Rosso | Local-language | 1.10 | Free web, paid print guide | Local-language anchor (Italy) |
| Guia Repsol | Local-language | 1.10 | Free | Local-language anchor (Spain/Portugal) |
| Le Fooding | Local-language | 1.10 | Free | Local-language anchor (France) |
| Gault&Millau | Local-language | 1.10 | Free web, paid print guide | Local-language anchor (multi-country Europe) |
| Falstaff | Local-language | 1.10 | Free web, paid print guide | Local-language anchor (Austria/Germany) |
| OpenRice | Local-language | 1.10 | Free | Local-language anchor (Hong Kong) |
| Zomato | Local-language | 1.10 | Free | Local-language anchor (India, Middle East) |
| Kakao Map | Local-language | 1.10 | Free | Local-language anchor (Korea, secondary) |
| Yandex Maps | Local-language | 1.10 | Free | Local-language anchor (Russia, ex-Soviet) |
| Google Maps reviews | Local-language | 1.10 | Free | Floor-level fallback everywhere |
| HappyCow | Local-language | 1.10 | Free | Category specialist (vegan/vegetarian) |
| TripAdvisor | Local-language | 1.10 | Free | Floor-level fallback, corroborate only |
| Foursquare City Guide | Local-language | 1.10 | n/a | Defunct, do not use |
| Reddit country/city subreddits | Community | 1.11 | Free | Community, corroborate only |
| Hungry Onion / Food Talk Central | Community | 1.11 | Free | Community, corroborate only |
