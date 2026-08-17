# -*- coding: utf-8 -*-
"""Worked end-to-end build. Copy into <trip>/scripts/ and edit the CONFIG block.

    py build_trip.py                 build from <trip>/research/*.psv
    py build_trip.py --demo          run the built-in fixture into a temp folder
                                     (smoke test for the whole toolchain)

Wires the record set to all five deliverables:
    1. master itinerary            .docx
    2. per-city site guides        .docx
    3. editorial guides            .docx  (one per source family present)
    4. Google Maps CSV sets        .csv
    5. reservation tracker         .docx
"""
import os
import sys
from datetime import date, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_SCRIPTS = os.path.join(os.path.dirname(HERE), 'scripts')
for p in (SKILL_SCRIPTS, HERE, os.path.join(HERE, '..', 'scripts')):
    if os.path.isdir(p) and p not in sys.path:
        sys.path.insert(0, p)

import records as R           # noqa: E402
import hours as H             # noqa: E402
import maps_csv               # noqa: E402
import tripdoc as T           # noqa: E402
import validate_records as V  # noqa: E402

# =========================================================== CONFIG

TRIP = r"<WORKSPACE>/YYYY-MM-DD-DESTINATION-itinerary"
DESTINATION = "Destination"
DATE_FROM = (2026, 7, 18)
DATE_TO = (2026, 7, 31)
EDITORIAL_SOURCES = ('CNT', 'NYT36', 'Eater', 'Michelin')

# Per-city day sequencing. One dict per day. The Closed today column is filled
# automatically from the record hours if left out.
SEQUENCE = {
    # 'Tokyo': [
    #     dict(day='Sat Jul 18', theme='Arrival, west side',
    #          morning='...', midday='...', late='...', evening='...'),
    # ],
}

# ===========================================================


def trip_dates():
    d0, d1 = date(*DATE_FROM), date(*DATE_TO)
    out, d = [], d0
    while d <= d1:
        out.append(d)
        d += timedelta(days=1)
    return out


def fill_closed_column(recs, city, sequence):
    """Populate each day's 'closed' cell from the anchor records' weekly hours."""
    anchors = [r for r in recs if r['city'] == city and r['tier'] == 'anchor']
    for row in sequence:
        if row.get('closed'):
            continue
        try:
            parts = row['day'].split()
            d = None
            for fmt_day in parts:
                if fmt_day.isdigit():
                    pass
            d = row.get('_date')
        except Exception:
            d = None
        if d is None:
            continue
        shut = H.closed_today_line(anchors, d)
        row['closed'] = ', '.join(shut[:4]) + ('...' if len(shut) > 4 else '') or 'nothing'
    return sequence


def build(trip, destination, recs, sequence=None, date_span=None):
    out = []
    label = '%s  |  %s to %s' % (
        destination,
        '%04d.%02d.%02d' % DATE_FROM if date_span is None else date_span[0],
        '%04d.%02d.%02d' % DATE_TO if date_span is None else date_span[1])
    stamp = '%04d.%02d.%02d' % DATE_FROM

    # ---- 2. per-city site guides
    for city in R.cities(recs):
        cr = [r for r in recs if r['city'] == city]
        seq = (sequence or {}).get(city)
        p = os.path.join(trip, '%s %s Sites Guide.docx' % (stamp[:7], city))
        out.append(T.build_site_guide(p, city, cr, sequence=seq))

    # ---- 3. editorial guides
    for src in EDITORIAL_SOURCES:
        hits = [r for r in recs if src in R.source_list(r)]
        if not hits:
            continue
        for city in R.cities(hits):
            cr = [r for r in hits if r['city'] == city]
            if len(cr) < 3:
                continue
            p = os.path.join(trip, '%s Guide - %s.docx' % (src, city))
            out.append(T.build_editorial_guide(
                p, city, cr, src,
                outline=['%d places across %d categories.'
                         % (len(cr), len({r['category'] for r in cr})),
                         'Filtered to the travel dates: no hotels, no lodging, '
                         'no out-of-season picks.']))

    # ---- 5. reservation tracker
    backups = {}
    for r in recs:
        if r['tier'] != 'anchor':
            continue
        backups[r['name']] = [x for x in recs
                              if x is not r and x['city'] == r['city']
                              and x['cluster'] == r['cluster']
                              and x['category'] == r['category']
                              and x['tier'] != 'anchor']
    p = os.path.join(trip, '%s Reservation Tracker.docx' % stamp)
    out.append(T.build_reservation_tracker(p, recs, label, backups=backups))

    # ---- 1. master itinerary skeleton
    out.append(build_itinerary(os.path.join(
        trip, '%s %s Itinerary.docx' % (stamp, destination)), destination, recs))

    # ---- 4. maps csvs
    maps_csv.write_all(recs, trip, editorial_sources=EDITORIAL_SOURCES)

    return out


def build_itinerary(path, destination, recs):
    """Master itinerary. The day-by-day body is trip-specific; this builds the
    fixed scaffolding (at-a-glance, pivots, booking actions, masters) so the
    hand-written days drop into section 5."""
    doc = T.Doc(destination, 'Itinerary  |  %04d.%02d.%02d to %04d.%02d.%02d'
                % (DATE_FROM + DATE_TO),
                'Hours in compact notation (M Tu W Th F Sa Su, 24-hour, CLOSED '
                'marks the weekly closure). Every venue line carries hours, a '
                'booking lead time, and a price range in local currency and USD.')

    doc.h1('At a Glance')
    doc.para('One page. Everything else is detail.', size=9, italic=True,
             color=T.GREY, after=4)
    rows = []
    for d in trip_dates():
        rows.append([d.strftime('%a %b %d'), '', '', '', '', ''])
    doc.table(['Date', 'Base', 'Theme', 'Anchor', 'Evening', 'Booked?'], rows,
               widths=[1.0, 1.0, 2.0, 2.3, 2.3, 0.8])
    doc.page_break()

    doc.h1('Fixed Pivots and Collisions')
    doc.para('The immovable dates that set the trip direction. Resolve these '
             'before writing any day.', size=9, italic=True, color=T.GREY, after=4)
    dated = [r for r in recs if (r.get('closed') or '').strip()
             or r['res'] in ('RES:lottery', 'RES:3-6mo')]
    if dated:
        for r in sorted(dated, key=lambda x: x['city']):
            doc.bullet('%s. %s' % (r.get('closed') or r['res'], r['note'][:120]),
                       bold_lead='%s (%s):' % (r['name'], r['city']))
    else:
        doc.para('None identified in the record set. Confirm festivals, '
                 'fixtures, holidays, and seasonal closures before building days.',
                 italic=True, color=T.GREY)

    doc.h1('Booking Actions by Deadline')
    for tag in R.RES_TAGS:
        group = [r for r in R.needs_booking(recs) if r['res'] == tag]
        if not group:
            continue
        doc.h3(tag.replace('RES:', 'Book '))
        for r in group:
            doc.bullet('%s. %s. %s' % (r.get('res_how') or 'method unconfirmed',
                                       r.get('price') or 'cost unconfirmed',
                                       r['note'][:110]),
                       bold_lead='%s (%s):' % (r['name'], r['city']),
                       flag='VERIFY' if 'verify-open' in R.flag_list(r) else None)

    doc.page_break()
    doc.h1('Logistics')
    for b in ['Arrival and transfer:', 'Rail or transit pass, with the '
              'break-even arithmetic:', 'Stored-value card:', 'Luggage '
              'forwarding:', 'Connectivity:', 'Cash versus card:',
              'Driving licence and International Driving Permit, if driving:',
              'Tax refund threshold and process:']:
        doc.bullet('to be filled', bold_lead=b)

    doc.page_break()
    doc.h1('Day by Day')
    doc.para('Hand-written per trip. One H2 per day, then morning / midday / '
             'late afternoon / evening sub-bullets. Every dinner slot carries an '
             'anchor plus two alternates.', size=9.5, italic=True, color=T.GREY)

    doc.page_break()
    doc.h1('Dining Master List')
    for city in R.cities(recs):
        cr = R.by(recs, city=city, category='Dining')
        if not cr:
            continue
        doc.h2(city)
        rows = [[r['name'], r['subcategory'], r['neighborhood'],
                 T.hours_cell(r), T.res_short(r), r.get('price', ''),
                 r['tier'], r['note'][:90]] for r in
                sorted(cr, key=lambda x: (x['cluster'], R.TIERS.index(x['tier'])))]
        doc.table(['Place', 'Genre', 'Neighborhood', 'Hours', 'Res', 'Price',
                   'Tier', 'Note'], rows,
                  widths=[1.4, 0.95, 1.1, 1.7, 0.95, 1.15, 0.6, 1.6])

    doc.h1('Retail and Craft Master List')
    for city in R.cities(recs):
        cr = R.by(recs, city=city, category=('Clothes', 'Shopping'))
        if not cr:
            continue
        doc.h2(city)
        rows = [[r['name'], r['category'].replace('Clothes', 'Menswear'),
                 r['subcategory'], r['neighborhood'], T.hours_cell(r),
                 r.get('price', ''), r['note'][:110]] for r in
                sorted(cr, key=lambda x: (x['category'], x['cluster'], x['name']))]
        doc.table(['Shop', 'Axis', 'Type', 'Neighborhood', 'Hours',
                   'Price', 'What to buy'], rows,
                  widths=[1.5, 0.9, 1.1, 1.15, 1.8, 1.1, 1.95])

    doc.h1('Assumptions and Open Questions')
    unk = [r for r in recs if (r.get('hours') or '').lower().startswith('unknown')]
    if unk:
        doc.bullet('%d record(s) shipped with unverified hours: %s'
                   % (len(unk), ', '.join(r['name'] for r in unk[:12])))
    single = [r for r in recs if len(R.source_list(r)) <= 1]
    if single:
        doc.bullet('%d record(s) rest on a single source and were not '
                   'independently corroborated.' % len(single))
    return doc.save(path)


# =========================================================== demo fixture

DEMO = """\
Tokyo || Dining || Omakase || Sushi Sho || 鮨さいとう || Sushi Sho Yotsuya Tokyo Japan || Yotsuya || Shinjuku-Yotsuya || Tu-Sa 18:00-22:00 (LO 20:30); CLOSED Su M || closed Aug 12-18 || RES:1-2mo || Pocket Concierge, releases on the 1st || ¥30,000-35,000 / $200-235 pp, no drinks || anchor || Edomae counter run at a punishing pace. The shari is warm and aggressively vinegared, which is the whole point. Order nothing, say nothing, eat as it lands. || Founded by a chef who left a Ginza institution to run a room where the rice, not the fish, is the argument. || books-out;cash-only || Research + Michelin
Tokyo || Dining || Omakase || Sushi Tokami || || Sushi Tokami Ginza Tokyo Japan || Ginza || Shinjuku-Yotsuya || M-Sa 12:00-14:00, 17:00-22:00; CLOSED Su || || RES:2-4wk || TableCheck || ¥22,000-28,000 / $145-185 pp || strong || Ginza counter known for aged tuna and a lighter hand with the vinegar. The substitute if the Yotsuya booking fails. || || || Research
Tokyo || Dining || Standing Sushi || Uogashi Nihon-Ichi || || Uogashi Nihon-Ichi Shibuya Tokyo Japan || Shibuya || Shinjuku-Yotsuya || daily 11:00-23:00 || || RES:walk-in || none || ¥2,000-3,500 / $13-23 pp || alternate || Standing counter, per-piece ordering, no reservation and no ceremony. The zero-risk sushi option in the same evening slot. || || || Research
Tokyo || Sights-Landmarks || Museum || Nezu Museum || 根津美術館 || Nezu Museum Minami-Aoyama Tokyo Japan || Minami-Aoyama || Aoyama-Omotesando || Tu-Su 10:00-17:00 (last entry 16:30); CLOSED M || closed for exhibition changeover late Jul || RES:none || none || ¥1,300 / $8.60 || anchor || Kengo Kuma's 2009 rebuild wraps a pre-war collection of Chinese bronzes in a long bamboo-flanked approach. The garden behind it is the reason to go. || Kuma's brief was to make a museum that reads as a roof, and the deep eaves and rammed-earth walls do exactly that. The garden holds four tea houses. || || Research + CNT
Tokyo || Clothes || Heritage Menswear || Beams Plus Harajuku || || Beams Plus Harajuku Tokyo Japan || Harajuku || Aoyama-Omotesando || daily 11:00-20:00 || || RES:none || none || ¥15,000-90,000 / $100-600 || anchor || The Ivy-and-workwear arm of Beams. Pleated wide-leg trousers, heavy oxford cloth, in-house takes on US military patterns. Ask for the Japan-exclusive lines. || || || Research + CNT
Kyoto || Sights-Sacred || Temple || Kiyomizu-dera || 清水寺 || Kiyomizu-dera Higashiyama Kyoto Japan || Higashiyama || East Kyoto: Higashiyama || daily 06:00-18:00 || || RES:none || none || ¥500 / $3.30 || anchor || Founded 778. The current halls date to 1633 under Tokugawa Iemitsu and the veranda is built without a single nail. Go at opening to beat the crowds. || The temple predates Kyoto as a capital and survived nine fires. The 1633 reconstruction is a deliberate act of Tokugawa legitimacy-building in a city that resented the shogunate. || UNESCO;stairs-heavy || Research + CNT + NYT36
Kyoto || Shopping || Knife Shop || Aritsugu || 有次 || Aritsugu Nishiki Market Kyoto Japan || Nakagyo || Central Kyoto: Nishiki || W-M 09:00-17:30; CLOSED Tu || || RES:none || walk in, sharpening while you wait || ¥12,000-60,000 / $80-400 || anchor || Founded 1560 as a swordsmith. Hand-forged carbon-steel kitchen blades, name engraved free while you wait, and a free sharpening lesson if you ask. || || cash-only || Research + CNT
"""


def demo():
    import tempfile
    trip = os.path.join(tempfile.gettempdir(), 'travelagent-demo')
    res = os.path.join(trip, 'research')
    os.makedirs(res, exist_ok=True)
    with open(os.path.join(res, 'demo.psv'), 'w', encoding='utf-8') as f:
        f.write(DEMO)
    recs = R.merge(R.load_dir(res))
    R.report(recs)
    errs, warns = V.check(recs, trip_dates())
    print('\nvalidate: %d errors, %d warnings' % (len(errs), len(warns)))
    for e in errs:
        print('  ERROR ' + e)
    for w in warns[:12]:
        print('  warn  ' + w)
    made = build(trip, 'Demo Trip', recs)
    print('\nbuilt:')
    for p in made:
        print('   %s  (%d bytes)' % (p, os.path.getsize(p)))
    return trip


def main():
    if '--demo' in sys.argv:
        demo()
        return 0
    res = os.path.join(TRIP, 'research')
    recs = R.merge(R.load_dir(res))
    R.report(recs)
    errs, warns = V.check(recs, trip_dates())
    if errs and '--force' not in sys.argv:
        print('\nBLOCKED: %d error(s). Fix them or pass --force.' % len(errs))
        for e in errs:
            print('  ' + e)
        return 1
    seq = {c: fill_closed_column(recs, c, SEQUENCE[c]) for c in SEQUENCE}
    for p in build(TRIP, DESTINATION, recs, sequence=seq):
        print(p)
    return 0


if __name__ == '__main__':
    sys.exit(main())
