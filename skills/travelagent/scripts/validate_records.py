# -*- coding: utf-8 -*-
"""Pre-flight gate. Fails the build on the violations that matter to this
traveler, so a bad record set never reaches a document.

    py validate_records.py <research dir> [--dates 2026-07-18:2026-07-31] [--warn-only]

Checks, in severity order:

  ERROR   missing or unparsable hours
  ERROR   missing or invalid reservation tag
  ERROR   dining anchor with a strict reservation and fewer than 2 same-cluster
          backups, or no zero-risk backup
  ERROR   em dash or en dash anywhere in any field
  ERROR   maps_query missing, or containing a URL
  ERROR   subcategory vocabulary over 30 values for one Maps layer
  WARN    hours are 'unknown, verify'
  WARN    anchor sight with a lottery or months-out booking and no alternate
  WARN    record with no note, or a note under 25 characters
  WARN    price missing on a Dining or Shopping record
  WARN    single-source record with no verify-open flag
  WARN    anchor closed on every date of the trip window (needs --dates)
  WARN    cluster with only one record (probably a stray, will render as a
          one-line section in the guide)

Exit code 0 clean, 1 if any ERROR fired (unless --warn-only).
"""
import sys
import re
from datetime import date, timedelta

import records as R
import hours as H

DASHES = ('—', '–')


def _dates(arg):
    a, b = arg.split(':')
    d0 = date(*[int(x) for x in a.split('-')])
    d1 = date(*[int(x) for x in b.split('-')])
    out, d = [], d0
    while d <= d1:
        out.append(d)
        d += timedelta(days=1)
    return out


def check(recs, trip_dates=None):
    errors, warns = [], []

    def E(rec, msg):
        errors.append('%-9s %-30s %s' % (rec.get('city', '?')[:9],
                                         rec.get('name', '?')[:30], msg))

    def W(rec, msg):
        warns.append('%-9s %-30s %s' % (rec.get('city', '?')[:9],
                                        rec.get('name', '?')[:30], msg))

    for r in recs:
        # -- hours
        hv = H.validate(r.get('hours'))
        if hv:
            hard = [x for x in hv if 'unparsed segment' not in x]
            if hard:
                E(r, 'hours: ' + '; '.join(hard))
            else:
                W(r, 'hours: ' + '; '.join(hv))
        if (r.get('hours') or '').lower().startswith('unknown'):
            W(r, 'hours unknown, must be verified before the doc ships')

        # -- reservation tag
        if not r.get('res'):
            E(r, 'res tag is blank; RES:none is the valid "nothing needed" value')
        elif r['res'] not in R.RES_TAGS:
            E(r, 'res tag %r is not in the vocabulary' % r['res'])
        elif R.RES_RANK[r['res']] <= R.RES_RANK['RES:2-4wk'] and not r.get('res_how'):
            W(r, 'strict res tag %s with no res_how (where does he book it?)' % r['res'])

        # -- dashes
        for k in R.FIELDS:
            v = r.get(k) or ''
            if any(d in v for d in DASHES):
                E(r, 'field %s contains an en/em dash' % k)

        # -- maps query
        mq = r.get('maps_query') or ''
        if not mq:
            E(r, 'maps_query is empty; geocoding will fall back to the bare name')
        elif mq.startswith('http'):
            E(r, 'maps_query is a URL; it must be a plain geocoding string')

        # -- note
        if len(r.get('note') or '') < 25:
            W(r, 'note is thin (%d chars); it is what shows in the Maps pin'
              % len(r.get('note') or ''))

        # -- price
        if r['category'] in ('Dining', 'Shopping', 'Clothes') and not r.get('price'):
            W(r, 'no price range on a %s record' % r['category'])

        # -- provenance
        if len(R.source_list(r)) <= 1 and 'verify-open' not in R.flag_list(r):
            W(r, 'single source (%s) and not flagged verify-open'
              % (r.get('source') or 'none'))

        # -- trip-window closure
        if trip_dates and r['tier'] == 'anchor':
            states = [H.is_open_on(r.get('hours'), d) for d in trip_dates]
            if states and all(s is False for s in states):
                W(r, 'anchor appears closed on every date of the trip window')

    # -- dining backup rule
    for rec, why in R.backup_gaps(recs):
        errors.append('%-9s %-30s BACKUP RULE: %s'
                      % (rec['city'][:9], rec['name'][:30], why))

    # -- sight anchors with brutal booking and no alternate
    for r in recs:
        if r['category'].startswith('Sights') and r['tier'] == 'anchor' \
                and r['res'] in ('RES:lottery', 'RES:3-6mo'):
            alts = [x for x in recs if x is not r and x['city'] == r['city']
                    and x['cluster'] == r['cluster'] and x['tier'] != 'anchor']
            if not alts:
                W(r, 'hard-to-book anchor sight (%s) with no alternate in its cluster'
                  % r['res'])

    # -- Maps layer subcategory load
    for (city, cat), subs in R.subcategory_load(recs).items():
        if len(subs) > 30:
            errors.append('%-9s %-30s LAYER: %d distinct subcategories, Maps '
                          'style-by-data caps near 30' % (city[:9], cat[:30], len(subs)))

    # -- thin clusters
    from collections import Counter
    cl = Counter((r['city'], r['cluster']) for r in recs if r['cluster'])
    for (city, cluster), n in sorted(cl.items()):
        if n == 1:
            warns.append('%-9s %-30s THIN CLUSTER: 1 record, fold it into a '
                         'neighbour' % (city[:9], cluster[:30]))

    return errors, warns


def main():
    args = [a for a in sys.argv[1:]]
    if not args:
        print(__doc__)
        return 0
    directory = args[0]
    trip_dates = None
    warn_only = '--warn-only' in args
    for i, a in enumerate(args):
        if a == '--dates' and i + 1 < len(args):
            trip_dates = _dates(args[i + 1])

    recs = R.merge(R.load_dir(directory))
    R.report(recs)
    errors, warns = check(recs, trip_dates)

    print()
    if errors:
        print('ERRORS (%d) -- build is blocked' % len(errors))
        print('-' * 78)
        for e in errors:
            print('  ' + e)
    else:
        print('ERRORS: none')
    print()
    if warns:
        print('WARNINGS (%d)' % len(warns))
        print('-' * 78)
        for w in warns[:60]:
            print('  ' + w)
        if len(warns) > 60:
            print('  ... and %d more' % (len(warns) - 60))
    else:
        print('WARNINGS: none')
    print()
    if errors and not warn_only:
        print('FAIL. Fix the errors or re-run with --warn-only to inspect anyway.')
        return 1
    print('PASS.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
