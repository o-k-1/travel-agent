# -*- coding: utf-8 -*-
"""Load, parse, merge, and query the canonical place records.

Records arrive from research subagents as pipe-delimited (' || ') lines with a
strict 18-field count. See references/data-schema.md.

Usage:
    import records
    rs = records.load_dir('<trip>/research')
    rs = records.merge(rs)
    records.report(rs)
    dining = records.by(rs, city='Tokyo', category='Dining')
    gaps   = records.backup_gaps(rs)
"""
import os
import re
import glob
from urllib.parse import quote

FIELDS = ['city', 'category', 'subcategory', 'name', 'local_name', 'maps_query',
          'neighborhood', 'cluster', 'hours', 'closed', 'res', 'res_how',
          'price', 'tier', 'note', 'why', 'flags', 'source']
N_FIELDS = len(FIELDS)

CATEGORIES = ['Dining', 'Clothes', 'Shopping', 'Sights-Sacred',
              'Sights-Landmarks', 'Activities', 'Nightlife', 'Logistics']

RES_TAGS = ['RES:3-6mo', 'RES:1-2mo', 'RES:2-4wk', 'RES:1wk', 'RES:2-3d',
            'RES:same-day', 'RES:walk-in', 'RES:lottery', 'RES:concierge', 'RES:none']
# strictness ordering, index 0 is the most demanding
RES_RANK = {t: i for i, t in enumerate(RES_TAGS)}
# anything at or stricter than RES:2-4wk needs backups per the traveler's rule
STRICT_CUTOFF = RES_RANK['RES:2-3d']

TIERS = ['anchor', 'strong', 'alternate']

_ENTITIES = [('&amp;', 'and'), ('&AMP;', 'and'), ('&#38;', 'and'), ('&', 'and'),
             ('&#39;', "'"), ('&rsquo;', "'"), ('&lsquo;', "'"),
             ('&quot;', '"'), ('&ldquo;', '"'), ('&rdquo;', '"'),
             ('&nbsp;', ' '), ('&mdash;', ', '), ('&ndash;', '-'),
             ('—', ', '), ('–', '-')]


# ---------------------------------------------------------------- helpers

def clean_field(s):
    """Normalize entities and dashes. Em dashes are banned in all output."""
    s = (s or '').strip()
    for a, b in _ENTITIES:
        s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s).strip()


def norm_name(n):
    return re.sub(r'[^a-z0-9]', '', (n or '').lower())


def maps_url(query):
    return 'https://www.google.com/maps/search/?api=1&query=' + quote(query or '')


def flag_list(rec):
    return [f.strip() for f in (rec.get('flags') or '').split(';') if f.strip()]


def source_list(rec):
    return [s.strip() for s in re.split(r'\s*\+\s*|\s*,\s*', rec.get('source') or '') if s.strip()]


def price_band(rec):
    """Coarse band from the USD figure in the price string, for backup matching.
    Returns 0 (unknown), 1 (<$25), 2 ($25-75), 3 ($75-200), 4 (>$200)."""
    m = re.findall(r'\$\s*([\d,]+)', rec.get('price') or '')
    if not m:
        return 0
    vals = [int(x.replace(',', '')) for x in m]
    v = sum(vals) / float(len(vals))
    if v < 25:
        return 1
    if v < 75:
        return 2
    if v < 200:
        return 3
    return 4


# ---------------------------------------------------------------- loading

def parse_line(line, origin=''):
    """Parse one ' || ' line. Returns (record, error_string)."""
    line = line.rstrip('\n').rstrip('\r')
    if not line.strip():
        return None, None
    if line.lstrip().startswith(('#', '```')):
        return None, None
    parts = [clean_field(p) for p in line.split('||')]
    if len(parts) != N_FIELDS:
        return None, '%s: expected %d fields, got %d: %s' % (
            origin, N_FIELDS, len(parts), line[:110])
    rec = dict(zip(FIELDS, parts))
    if rec['city'].lower() == 'city' and rec['name'].lower() == 'name':
        return None, None                      # header row the agent emitted anyway
    if not rec['name']:
        return None, '%s: record with no name: %s' % (origin, line[:110])
    if rec['category'] not in CATEGORIES:
        rec['flags'] = (rec['flags'] + ';' if rec['flags'] else '') + 'category-fixed'
        rec['category'] = ('Dining' if 'din' in rec['category'].lower()
                           else 'Sights-Landmarks')
    if rec['res'] and not rec['res'].upper().startswith('RES:'):
        rec['res'] = 'RES:' + rec['res'].strip().lstrip(':')
    if rec['res'] not in RES_TAGS:
        rec['res'] = rec['res'] or 'RES:none'
    if rec['tier'] not in TIERS:
        rec['tier'] = 'strong' if rec['tier'] else 'strong'
    rec['_origin'] = origin
    return rec, None


def load_file(path):
    """Returns (records, errors)."""
    recs, errs = [], []
    origin = os.path.basename(path)
    with open(path, encoding='utf-8', errors='replace') as f:
        for line in f:
            r, e = parse_line(line, origin)
            if r:
                recs.append(r)
            elif e:
                errs.append(e)
    return recs, errs


def load_dir(directory, pattern='*.psv'):
    """Load every matching file in a directory. Prints a dropped-line log."""
    all_recs, all_errs = [], []
    for p in sorted(glob.glob(os.path.join(directory, pattern))):
        r, e = load_file(p)
        all_recs.extend(r)
        all_errs.extend(e)
    if all_errs:
        print('DROPPED %d malformed line(s):' % len(all_errs))
        for e in all_errs[:25]:
            print('  ' + e)
        if len(all_errs) > 25:
            print('  ... and %d more' % (len(all_errs) - 25))
    return all_recs


def write_psv(recs, path):
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        for r in recs:
            f.write(' || '.join(r.get(k, '') for k in FIELDS) + '\n')
    return len(recs)


# ---------------------------------------------------------------- merging

def merge(recs, verbose=True):
    """Dedupe on (city, normalized name). Unions sources and flags, keeps the
    richer note, the more specific hours, and the stricter res tag."""
    out, index = [], {}
    dupes = 0
    for r in recs:
        key = (r['city'], norm_name(r['name']))
        if key not in index:
            index[key] = r
            out.append(r)
            continue
        dupes += 1
        base = index[key]
        # sources: union, Research first, then alphabetical
        srcs = set(source_list(base)) | set(source_list(r))
        base['source'] = ' + '.join(sorted(srcs, key=lambda s: (s != 'Research', s)))
        # flags: union
        fl = set(flag_list(base)) | set(flag_list(r))
        base['flags'] = ';'.join(sorted(fl))
        # note: keep materially longer
        if len(r['note']) > len(base['note']) + 15:
            base['note'] = r['note']
        # why: keep the longer writeup
        if len(r['why']) > len(base['why']):
            base['why'] = r['why']
        # hours: prefer a parsable spec over 'unknown'
        if base['hours'].lower().startswith('unknown') and not r['hours'].lower().startswith('unknown'):
            base['hours'] = r['hours']
        # res: keep the stricter
        if RES_RANK.get(r['res'], 99) < RES_RANK.get(base['res'], 99):
            base['res'] = r['res']
            base['res_how'] = r['res_how'] or base['res_how']
        # fill blanks the base lacks
        for k in ('local_name', 'price', 'res_how', 'closed', 'cluster',
                  'neighborhood', 'subcategory', 'maps_query'):
            if not base.get(k) and r.get(k):
                base[k] = r[k]
        # tier: keep the strongest
        if TIERS.index(r['tier']) < TIERS.index(base['tier']):
            base['tier'] = r['tier']
    if verbose:
        print('merged %d records into %d (%d duplicates folded)'
              % (len(recs), len(out), dupes))
    return out


def consensus(recs, min_sources=3):
    """Records independently corroborated by min_sources or more."""
    return [r for r in recs if len(source_list(r)) >= min_sources]


# ---------------------------------------------------------------- queries

def by(recs, **kw):
    """by(recs, city='Tokyo', category='Dining', tier='anchor')"""
    out = recs
    for k, v in kw.items():
        if isinstance(v, (list, tuple, set)):
            out = [r for r in out if r.get(k) in v]
        else:
            out = [r for r in out if r.get(k) == v]
    return out


def cities(recs):
    order = ['Tokyo', 'Kyoto', 'Osaka', 'DayTrip', 'Other']
    found = sorted({r['city'] for r in recs},
                   key=lambda c: (order.index(c) if c in order else 50, c))
    return found


def clusters(recs, city):
    """Clusters in the order they first appear, which is the research order."""
    seen, out = set(), []
    for r in recs:
        if r['city'] == city and r['cluster'] and r['cluster'] not in seen:
            seen.add(r['cluster'])
            out.append(r['cluster'])
    return out


def needs_booking(recs, cutoff='RES:2-3d'):
    """Everything worth a row in the reservation tracker, strictest first."""
    lim = RES_RANK[cutoff]
    hits = [r for r in recs if RES_RANK.get(r['res'], 99) <= lim]
    return sorted(hits, key=lambda r: (RES_RANK.get(r['res'], 99), r['city'], r['name']))


ZERO_RISK = ('RES:walk-in', 'RES:same-day', 'RES:none')


def backups_for(rec, recs):
    """Every non-anchor Dining record in the same city and cluster."""
    return [x for x in recs
            if x is not rec
            and x['category'] == rec['category']
            and x['city'] == rec['city']
            and x['cluster'] == rec['cluster']
            and x['tier'] != 'anchor']


def backup_gaps(recs):
    """The traveler's hard rule: every Dining anchor with a reservation stricter
    than RES:2-3d needs, in the same cluster:

        a) two or more non-anchor records, AND
        b) at least one true PEER (within one price band, so the evening is not
           downgraded when the booking falls through), AND
        c) at least one ZERO-RISK option (walk-in, same-day, or no booking).

    (b) and (c) are deliberately separate tests. A cheap standing counter is a
    perfectly good zero-risk fallback for a splurge omakase even though it is
    nothing like a price peer, so the zero-risk test ignores price entirely.

    Returns a list of (record, problem) tuples. Empty list means the rule holds.
    """
    gaps = []
    for r in recs:
        if r['category'] != 'Dining' or r['tier'] != 'anchor':
            continue
        if RES_RANK.get(r['res'], 99) > STRICT_CUTOFF:
            continue
        pool = backups_for(r, recs)
        band = price_band(r)
        peers = [x for x in pool
                 if band == 0 or price_band(x) == 0 or abs(price_band(x) - band) <= 1]
        zero = [x for x in pool if x['res'] in ZERO_RISK]
        if len(pool) < 2:
            gaps.append((r, 'only %d same-cluster backup(s) in "%s", needs 2'
                         % (len(pool), r['cluster'])))
        elif not peers:
            gaps.append((r, 'no same-price-band peer among %d backup(s) in "%s"'
                         % (len(pool), r['cluster'])))
        elif not zero:
            gaps.append((r, 'no zero-risk (walk-in / same-day) backup in "%s"'
                         % r['cluster']))
    return gaps


def subcategory_load(recs):
    """Distinct subcategory count per (city, category). Google My Maps
    style-by-data categorize tops out around 30 groups per layer."""
    load = {}
    for r in recs:
        load.setdefault((r['city'], r['category']), set()).add(r['subcategory'])
    return {k: sorted(v) for k, v in load.items()}


# ---------------------------------------------------------------- reporting

def report(recs):
    from collections import Counter
    print('=' * 66)
    print('%d records, %d cities' % (len(recs), len(cities(recs))))
    print('=' * 66)
    for c in cities(recs):
        cr = [r for r in recs if r['city'] == c]
        cc = Counter(r['category'] for r in cr)
        line = '  '.join('%s %d' % (k, cc[k]) for k in CATEGORIES if cc[k])
        print('%-12s %4d   %s' % (c, len(cr), line))
    print('-' * 66)
    tc = Counter(r['tier'] for r in recs)
    print('tiers:   ' + '  '.join('%s %d' % (t, tc[t]) for t in TIERS))
    rc = Counter(r['res'] for r in recs)
    print('res:     ' + '  '.join('%s %d' % (t, rc[t]) for t in RES_TAGS if rc[t]))
    con = consensus(recs)
    print('consensus picks (3+ sources): %d' % len(con))
    gaps = backup_gaps(recs)
    print('dining backup-rule gaps: %d' % len(gaps))
    for r, why in gaps[:10]:
        print('   ! %s (%s): %s' % (r['name'], r['city'], why))
    over = {k: v for k, v in subcategory_load(recs).items() if len(v) > 30}
    if over:
        print('subcategory overload (>30 per Maps layer):')
        for k, v in over.items():
            print('   ! %s / %s: %d distinct' % (k[0], k[1], len(v)))
    print('=' * 66)


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        rs = merge(load_dir(sys.argv[1]))
        report(rs)
    else:
        print(__doc__)
        print('fields (%d): %s' % (N_FIELDS, ', '.join(FIELDS)))
        print('res tags:   %s' % ', '.join(RES_TAGS))
        print('categories: %s' % ', '.join(CATEGORIES))
