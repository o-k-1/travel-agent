# -*- coding: utf-8 -*-
"""Write the Google My Maps import CSV sets.

Three sets, per references/deliverables-spec.md:
    MAPS - Master/          one file per city, all categories, deduped
    MAPS - By Category/     city x category, for maximum icon control
    MAPS - Editorial/       one per source family per city, plus a combined file

The Note column is composed so the pin popup carries the compact hours and the
reservation flag inline, which is what the traveler asked for:

    Omakase | Tu-Sa 18:00-22:00; CLOSED Su M | RES 1-2mo via Pocket Concierge | <note> | ¥30,000 / $200

Encoding is utf-8-sig on every file so Excel opens local script correctly.

Usage:
    import records, maps_csv
    rs = records.merge(records.load_dir(trip + '/research'))
    maps_csv.write_all(rs, trip)
"""
import os
import csv
import re

import records as R
import hours as H

HEADER = ['Name', 'Location', 'Category', 'Subcategory', 'Neighborhood',
          'Hours', 'Res', 'Price', 'Note', 'Source', 'MapsURL']
HEADER_COMBINED = ['Name', 'Location', 'City'] + HEADER[2:]

NOTE_MAX = 350
CAT_ORDER = R.CATEGORIES


def _safe(name):
    return re.sub(r'[^A-Za-z0-9 &-]', '', name).strip().replace(' ', '-')


def res_phrase(rec):
    """Human-readable reservation clause for the note field."""
    tag = rec.get('res') or 'RES:none'
    how = (rec.get('res_how') or '').strip()
    if how.lower() in ('none', 'n/a', 'na', '-', 'no', 'nothing'):
        how = ''            # agents write "none" here; it is noise in the pin
    words = {
        'RES:3-6mo': 'RES 3-6mo ahead',
        'RES:1-2mo': 'RES 1-2mo ahead',
        'RES:2-4wk': 'RES 2-4wk ahead',
        'RES:1wk': 'RES 1wk ahead',
        'RES:2-3d': 'RES 2-3 days ahead',
        'RES:same-day': 'RES same-day / timed entry',
        'RES:walk-in': 'walk-in, no booking',
        'RES:lottery': 'LOTTERY ballot',
        'RES:concierge': 'RES via concierge only',
        'RES:none': 'no booking needed',
    }
    base = words.get(tag, tag)
    if how and tag not in ('RES:none', 'RES:walk-in'):
        return '%s via %s' % (base, how)
    if how and tag == 'RES:walk-in':
        return '%s (%s)' % (base, how)
    return base


def compose_note(rec):
    """<Subcategory> | <hours> | <res> | <note> | <price>, with the closure
    warning promoted into the hours segment."""
    parts = []
    if rec.get('subcategory'):
        parts.append(rec['subcategory'])

    hrs = H.for_note(rec.get('hours') or 'unknown, verify')
    closed = (rec.get('closed') or '').strip()
    if closed:
        hrs = '%s; %s' % (hrs, closed)
    parts.append(hrs)

    parts.append(res_phrase(rec))

    if rec.get('note'):
        parts.append(rec['note'])

    fl = [f for f in R.flag_list(rec)
          if f in ('UNESCO', 'verify-open', 'no-photography', 'cash-only', 'seasonal')]
    if fl:
        parts.append('[' + ', '.join(fl) + ']')

    if rec.get('price'):
        parts.append(rec['price'])

    note = ' | '.join(p for p in parts if p)
    if len(note) > NOTE_MAX:
        note = note[:NOTE_MAX - 3].rstrip() + '...'
    return note


def _row(rec, with_city=False):
    base = [rec['name'], rec['maps_query'] or rec['name']]
    if with_city:
        base.append(rec['city'])
    return base + [rec['category'], rec['subcategory'], rec['neighborhood'],
                   H.for_note(rec.get('hours') or 'unknown, verify'),
                   res_phrase(rec), rec.get('price', ''),
                   compose_note(rec), rec.get('source', ''),
                   R.maps_url(rec['maps_query'] or rec['name'])]


def _sort_key(rec):
    ci = CAT_ORDER.index(rec['category']) if rec['category'] in CAT_ORDER else 99
    ti = R.TIERS.index(rec['tier']) if rec['tier'] in R.TIERS else 9
    return (ci, rec['subcategory'], ti, rec['name'])


def write_csv(recs, path, with_city=False):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    rows = sorted(recs, key=_sort_key)
    hdr = HEADER_COMBINED if with_city else HEADER
    with open(path, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.writer(f)
        w.writerow(hdr)
        for r in rows:
            w.writerow(_row(r, with_city))
    return len(rows)


# ---------------------------------------------------------------- the 3 sets

def write_master(recs, trip, folder='MAPS - Master', version=''):
    """One file per city. The set to actually import."""
    suffix = ('-' + version) if version else ''
    out = os.path.join(trip, folder + (' ' + version if version else ''))
    total = {}
    for city in R.cities(recs):
        cr = [r for r in recs if r['city'] == city]
        p = os.path.join(out, '%s-MASTER%s.csv' % (_safe(city), suffix))
        total[os.path.basename(p)] = write_csv(cr, p)
    _write_import_guide(out, recs)
    return out, total


def write_by_category(recs, trip, folder='MAPS - By Category'):
    """city x category. Skips empty combinations."""
    out = os.path.join(trip, folder)
    total = {}
    for city in R.cities(recs):
        for cat in CAT_ORDER:
            cr = [r for r in recs if r['city'] == city and r['category'] == cat]
            if not cr:
                continue
            p = os.path.join(out, '%s-%s.csv' % (_safe(city), _safe(cat)))
            total[os.path.basename(p)] = write_csv(cr, p)
    _write_import_guide(out, recs)
    return out, total


def write_editorial(recs, trip, source_tag, folder='MAPS - Editorial'):
    """One file per city for records carrying source_tag, plus a combined
    mass-upload file across all cities."""
    out = os.path.join(trip, folder)
    hits = [r for r in recs if source_tag in R.source_list(r)]
    total = {}
    for city in R.cities(hits):
        cr = [r for r in hits if r['city'] == city]
        p = os.path.join(out, '%s-%s.csv' % (_safe(source_tag), _safe(city)))
        total[os.path.basename(p)] = write_csv(cr, p)
    p = os.path.join(out, '%s-ALL-mass-upload.csv' % _safe(source_tag))
    total[os.path.basename(p)] = write_csv(hits, p, with_city=True)
    _write_import_guide(out, hits)
    return out, total


def write_all(recs, trip, editorial_sources=('CNT', 'NYT36', 'Eater')):
    made = []
    d, t = write_master(recs, trip)
    made.append((d, t))
    d, t = write_by_category(recs, trip)
    made.append((d, t))
    for s in editorial_sources:
        if any(s in R.source_list(r) for r in recs):
            d, t = write_editorial(recs, trip, s)
            made.append((d, t))
    for d, t in made:
        print('\n%s' % d)
        for fn in sorted(t):
            print('   %-44s %4d rows' % (fn, t[fn]))
    return made


# ---------------------------------------------------------------- guide file

_GUIDE = """GOOGLE MY MAPS IMPORT GUIDE
===========================

Import target is Google MY MAPS, not Google Maps saved lists.
Saved lists have NO bulk import. My Maps does.

STEPS
  1. Open https://mymaps.google.com and click "Create a new map".
  2. Click "Import" under the untitled layer.
  3. Upload ONE csv. One csv becomes one layer.
  4. Column to position placemarks: choose  Location
  5. Column to title markers:      choose  Name
  6. Repeat "Add layer" then "Import" for each additional csv.

DIFFERENT ICONS PER TYPE
  Inside a layer, click "Style by data column" then pick  Subcategory
  and choose "Categorize". Each distinct Subcategory value gets its own
  icon and colour, which you can then change individually.
  Practical cap is about 30 groups per layer, which is why the
  subcategory vocabulary is kept tight.

LIMITS
  10 layers per map. 2,000 features per layer. 10 MB per csv.
  If a city exceeds a layer, use the MAPS - By Category set instead
  of the master file for that city.

THE NOTE COLUMN
  Each pin's description carries, in order:
    Subcategory | opening hours | reservation requirement | what it is
    known for and what to get | flags | price range
  Compact hours notation: day tokens are M Tu W Th F Sa Su, times are
  24-hour, "CLOSED <days>" in caps marks the weekly closure, "LO" is
  last order, "last entry" is the museum cutoff.

ACCURACY CAVEAT
  Geocoding runs off the Location string and is imperfect for small
  owner-operated venues. Spot-check pins whose Note carries
  [verify-open]. Google Maps hours for small venues are frequently
  stale; the Hours column here reflects the source that was checked,
  not Google's listing.

CONTENTS OF THIS FOLDER
%s
"""


def _write_import_guide(folder, recs):
    os.makedirs(folder, exist_ok=True)
    from collections import Counter
    cc = Counter(r['category'] for r in recs)
    body = '\n'.join('  %-20s %4d' % (k, cc[k]) for k in CAT_ORDER if cc[k])
    body += '\n  %-20s %4d' % ('TOTAL', len(recs))
    with open(os.path.join(folder, 'README-import-guide.txt'), 'w',
              encoding='utf-8') as f:
        f.write(_GUIDE % body)


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 2:
        trip = sys.argv[1]
        rs = R.merge(R.load_dir(sys.argv[2]))
        R.report(rs)
        write_all(rs, trip)
    else:
        print(__doc__)
        print('usage: py maps_csv.py <trip folder> <research dir>')
