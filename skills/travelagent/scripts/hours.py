# -*- coding: utf-8 -*-
"""Compact operating-hours notation: parse, validate, normalize, and answer
"is this open on date D".

The notation is defined in references/hours-and-closures.md. Summary:

    daily 09:00-18:00
    M-F 09:00-17:00; CLOSED Sa Su
    Tu-Su 10:00-17:00 (last entry 16:30); CLOSED M
    Tu-Sa 11:30-14:00, 17:30-22:00 (LO 21:00); CLOSED Su M
    W-M 10:00-18:00; CLOSED Tu; CLOSED 3rd Wed
    24h
    always open
    by appointment
    irregular, check IG
    unknown, verify

Day tokens are M Tu W Th F Sa Su. Single-letter R for Thursday is rejected:
it is ambiguous with nothing but reads as a typo, and Th is unambiguous.

Usage:
    import hours
    hours.validate("Tu-Su 10:00-17:00; CLOSED M")     -> []
    hours.closed_days("Tu-Su 10:00-17:00; CLOSED M")  -> {'M'}
    hours.is_open_on("Tu-Su 10:00-17:00; CLOSED M", date(2026,7,20))  -> False
    hours.normalize("tu-su 10-17; closed m")          -> 'Tu-Su 10:00-17:00; CLOSED M'
"""
import re
from datetime import date as _date

DAYS = ['M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su']
DAY_INDEX = {d: i for i, d in enumerate(DAYS)}
# python weekday(): Monday=0 .. Sunday=6, which matches DAYS order exactly.

MARKERS = {
    '24h': 'open 24 hours',
    'always open': 'unenclosed public space, no hours',
    'by appointment': 'appointment only',
    'irregular': 'irregular hours, verify before going',
    'unknown': 'hours not established, must verify',
    'seasonal': 'hours vary by season, verify for the trip dates',
}

_DAY_ALIASES = {
    'mon': 'M', 'm': 'M',
    'tue': 'Tu', 'tues': 'Tu', 'tu': 'Tu',
    'wed': 'W', 'w': 'W',
    'thu': 'Th', 'thur': 'Th', 'thurs': 'Th', 'th': 'Th',
    'fri': 'F', 'f': 'F',
    'sat': 'Sa', 'sa': 'Sa',
    'sun': 'Su', 'su': 'Su',
}

_MONTHS_RE = ('Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec')

_TIME_RE = re.compile(r'^(\d{1,2})(?::(\d{2}))?$')
_RANGE_RE = re.compile(r'^(\d{1,2}(?::\d{2})?)\s*-\s*(\d{1,2}(?::\d{2})?)$')


class HoursError(ValueError):
    pass


# ---------------------------------------------------------------- day tokens

def _day_token(tok):
    """Normalize one day token. Raises HoursError on 'R' and on unknowns."""
    raw = tok.strip()
    low = raw.lower().rstrip('.')
    if low == 'r':
        raise HoursError("'R' is not an accepted day token, use 'Th' for Thursday")
    if low in _DAY_ALIASES:
        return _DAY_ALIASES[low]
    raise HoursError("unknown day token %r" % raw)


def expand_daylist(text):
    """'M-Th, Sa' -> ['M','Tu','W','Th','Sa'].  'daily' -> all 7."""
    text = text.strip()
    if text.lower() in ('daily', 'every day', 'all week'):
        return list(DAYS)
    out = []
    # allow comma or space separated groups; ranges use '-'
    for chunk in re.split(r'[,\s]+', text):
        if not chunk:
            continue
        if '-' in chunk:
            a, b = chunk.split('-', 1)
            ia, ib = DAY_INDEX[_day_token(a)], DAY_INDEX[_day_token(b)]
            if ia <= ib:
                out.extend(DAYS[ia:ib + 1])
            else:                      # wraps the week, e.g. W-M
                out.extend(DAYS[ia:] + DAYS[:ib + 1])
        else:
            out.append(_day_token(chunk))
    seen, uniq = set(), []
    for d in out:
        if d not in seen:
            seen.add(d)
            uniq.append(d)
    return uniq


def collapse_daylist(days):
    """['M','Tu','W','Th','Sa'] -> 'M-Th, Sa'.  All seven -> 'daily'."""
    idx = sorted({DAY_INDEX[d] for d in days})
    if not idx:
        return ''
    if len(idx) == 7:
        return 'daily'
    # prefer a week-wrapping range when the complement is one contiguous run,
    # so {M,W,Th,F,Sa,Su} renders as 'W-M' rather than 'M, W-Su'
    missing = sorted(set(range(7)) - set(idx))
    if len(missing) < len(idx) and missing == list(range(missing[0], missing[-1] + 1)):
        start, end = (missing[-1] + 1) % 7, (missing[0] - 1) % 7
        if start != end:
            return '%s-%s' % (DAYS[start], DAYS[end])
    groups, start, prev = [], idx[0], idx[0]
    for i in idx[1:]:
        if i == prev + 1:
            prev = i
            continue
        groups.append((start, prev))
        start = prev = i
    groups.append((start, prev))
    parts = []
    for a, b in groups:
        if a == b:
            parts.append(DAYS[a])
        elif b == a + 1:
            parts.append('%s %s' % (DAYS[a], DAYS[b]))
        else:
            parts.append('%s-%s' % (DAYS[a], DAYS[b]))
    return ', '.join(parts)


# ---------------------------------------------------------------- time ranges

def _norm_time(t):
    m = _TIME_RE.match(t.strip())
    if not m:
        raise HoursError('bad time %r' % t)
    h = int(m.group(1))
    mi = int(m.group(2) or 0)
    if h > 30 or mi > 59:
        raise HoursError('impossible time %r' % t)
    return '%02d:%02d' % (h, mi)


def _to_minutes(hhmm):
    h, m = hhmm.split(':')
    return int(h) * 60 + int(m)


def parse_ranges(text):
    """'11:30-14:00, 17:30-22:00' -> [('11:30','14:00'), ('17:30','22:00')]

    Bare-hour shorthand gets pm inference: '9-4' means 09:00-16:00, because
    that is what the notation reference documents ('M-Th 9-4'). Explicit
    times are never adjusted, so '18:00-02:00' still fails validation and
    has to be written '18:00-26:00'.
    """
    out = []
    for chunk in text.split(','):
        chunk = chunk.strip()
        if not chunk:
            continue
        m = _RANGE_RE.match(chunk)
        if not m:
            raise HoursError('bad time range %r' % chunk)
        ra, rb = m.group(1).strip(), m.group(2).strip()
        a, b = _norm_time(ra), _norm_time(rb)
        bare = ':' not in ra and ':' not in rb
        if bare and int(rb) <= int(ra) and int(rb) <= 12:
            b = '%02d:00' % (int(rb) + 12)
        out.append((a, b))
    if not out:
        raise HoursError('no time range found')
    return out


# ---------------------------------------------------------------- main parse

def parse(spec):
    """Parse a compact hours string.

    Returns a dict:
        open:     {day: [(start,end), ...]}  for days with stated hours
        closed:   set of day tokens explicitly marked CLOSED
        markers:  list of marker keys hit ('24h', 'unknown', ...)
        extras:   list of parenthetical notes, e.g. 'LO 21:00'
        notes:    list of segments that were not machine-parsable
        raw:      the input
    """
    res = {'open': {}, 'closed': set(), 'markers': [], 'extras': [],
           'notes': [], 'marker_notes': [], 'implicit': set(), 'raw': spec}
    if spec is None:
        res['markers'].append('unknown')
        return res
    text = str(spec).strip()
    if not text:
        res['markers'].append('unknown')
        return res

    # ', CLOSED ...' is a segment boundary in practice, not a time-range comma
    text = re.sub(r',\s*(?=\+?CLOSED\b)', '; ', text, flags=re.I)

    for seg in [s.strip() for s in text.split(';') if s.strip()]:
        low = seg.lower()

        # bare markers
        hit = None
        for key in MARKERS:
            if low.startswith(key) or low == key:
                hit = key
                break
        if hit and not _RANGE_RE.search(seg.replace(' ', '')):
            res['markers'].append(hit)
            tail = re.sub(r'^only\b', '', seg[len(hit):].strip(' ,;')).strip(' ,;')
            if tail:
                res['marker_notes'].append(tail)   # 'verify', 'check IG'
            continue

        # CLOSED <daylist>  /  CLOSED <freeform>
        # handles 'CLOSED M (+Tu if M is holiday)' and 'CLOSED 3rd-W (maintenance)'
        if low.lstrip('+').startswith('closed'):
            rest = seg.lstrip('+')[6:].strip().strip(',')
            quals = re.findall(r'\(([^)]*)\)', rest)
            if quals:
                res['notes'].append(seg)          # keep the full rule visible
                rest = re.sub(r'\([^)]*\)', ' ', rest).strip()
            if not rest:
                if not quals:
                    res['notes'].append(seg)
                continue
            try:
                for d in expand_daylist(rest):
                    res['closed'].add(d)
            except (HoursError, KeyError):
                if not quals:
                    res['notes'].append(seg)      # 'CLOSED 3rd Wed', 'CLOSED Aug 13-16'
            continue

        # pull parentheticals out first
        extras = re.findall(r'\(([^)]*)\)', seg)
        if extras:
            res['extras'].extend(e.strip() for e in extras)
            seg = re.sub(r'\([^)]*\)', ' ', seg).strip()

        # seasonal prefix: 'Apr-Oct 09:00-18:00', 'Nov-Mar 10:00-16:00'
        # A season-split venue has no single weekly pattern, so it is kept
        # verbatim rather than flattened. is_open_on then returns None for it,
        # which is the honest answer: pick the season before you can say.
        mo = re.match(r'^(%s)\s*-\s*(%s)\s+(.*)$' % (_MONTHS_RE, _MONTHS_RE), seg, re.I)
        if mo:
            res['markers'].append('seasonal')
            res['marker_notes'].append(seg)
            continue

        # '<daylist> 24h'  ->  treat as a full-day range
        m24 = re.match(r'^(.*?)\s+24\s*h(?:ours)?$', seg, re.I)
        if m24:
            try:
                for d in expand_daylist(m24.group(1)):
                    res['open'].setdefault(d, []).append(('00:00', '24:00'))
                continue
            except (HoursError, KeyError):
                pass

        # <daylist> <timeranges>
        m = re.match(r'^(.*?)\s+(\d{1,2}(?::\d{2})?\s*-\s*.*)$', seg)
        if not m:
            # a bare timerange with no daylist means every day
            try:
                ranges = parse_ranges(seg)
            except (HoursError, KeyError):
                res['notes'].append(seg)
                continue
            for d in DAYS:
                res['open'].setdefault(d, []).extend(ranges)
                res['implicit'].add(d)
            continue
        daypart, timepart = m.group(1), m.group(2)
        try:
            days = expand_daylist(daypart)
            ranges = parse_ranges(timepart)
        except (HoursError, KeyError):
            res['notes'].append(seg)
            continue
        for d in days:
            res['open'].setdefault(d, []).extend(ranges)

    # an explicit CLOSED always wins over an all-days default range
    for d in list(res['open']):
        if d in res['closed'] and d in res['implicit']:
            del res['open'][d]

    return res


# ---------------------------------------------------------------- validation

def validate(spec):
    """Return a list of human-readable problems. Empty list means clean."""
    problems = []
    if spec is None or not str(spec).strip():
        return ['hours is empty; use "unknown, verify" if genuinely unknown']
    text = str(spec)

    if '—' in text or '–' in text:
        problems.append('contains an en/em dash; use a plain hyphen')
    if re.search(r'\bR\b', text):
        problems.append("uses 'R' for Thursday; use 'Th'")
    if re.search(r'\b\d{1,2}\s*(am|pm)\b', text, re.I):
        problems.append('uses am/pm; the notation is 24-hour (09:00-17:00)')

    p = parse(text)
    if not p['open'] and not p['markers']:
        problems.append('no parsable open hours and no marker (24h / unknown / by appointment)')
    for n in p['notes']:
        if not re.search(r'\d', n) and 'closed' not in n.lower():
            problems.append('unparsed segment: %r' % n)

    overlap = sorted(set(p['open']) & p['closed'])
    if overlap:
        problems.append('day(s) both open and CLOSED: %s' % ', '.join(overlap))

    for d, ranges in p['open'].items():
        for a, b in ranges:
            if _to_minutes(b) <= _to_minutes(a) and _to_minutes(b) != 0:
                problems.append('range %s-%s does not advance; use 24h+ notation '
                                'for past-midnight (e.g. 18:00-26:00)' % (a, b))

    seen, uniq = set(), []            # dedupe, a 7-day spec should not shout 7 times
    for x in problems:
        if x not in seen:
            seen.add(x)
            uniq.append(x)
    return uniq


def normalize(spec):
    """Round-trip a spec into canonical form. Unparsable parts pass through."""
    p = parse(spec)
    segs = []
    # group days that share an identical range set
    bucket = {}
    for d, ranges in p['open'].items():
        key = tuple(ranges)
        bucket.setdefault(key, []).append(d)
    for key in sorted(bucket, key=lambda k: min(DAY_INDEX[d] for d in bucket[k])):
        days = collapse_daylist(bucket[key])
        times = ', '.join('%s-%s' % r for r in key)
        segs.append('%s %s' % (days, times))
    if p['extras']:
        if segs:
            segs[-1] += ' (%s)' % '; '.join(p['extras'])
        else:
            segs.append('(%s)' % '; '.join(p['extras']))
    for i, m in enumerate(p['markers']):
        note = p['marker_notes'][i] if i < len(p['marker_notes']) else ''
        segs.append('%s, %s' % (m, note) if note else m)
    if p['closed']:
        segs.append('CLOSED ' + collapse_daylist(sorted(p['closed'], key=lambda d: DAY_INDEX[d])))
    for n in p['notes']:
        segs.append(n if n.upper().startswith('CLOSED') else n)
    return '; '.join(segs) if segs else str(spec)


# ---------------------------------------------------------------- queries

def closed_days(spec):
    """Set of day tokens the venue is shut. Combines explicit CLOSED with
    the complement of stated open days (only when open days were parsed)."""
    p = parse(spec)
    out = set(p['closed'])
    if p['open'] and not any(m in ('24h', 'always open') for m in p['markers']):
        out |= (set(DAYS) - set(p['open']))
    return out


def is_open_on(spec, d):
    """True / False / None (unknown) for a datetime.date.

    Only answers the weekly pattern. Date-specific closures live in the
    record's `closed` field, not here.
    """
    p = parse(spec)
    if any(m in ('24h', 'always open') for m in p['markers']):
        return True
    if 'unknown' in p['markers'] or 'irregular' in p['markers']:
        return None
    tok = DAYS[d.weekday()]
    if tok in p['closed']:
        return False
    if p['open']:
        return tok in p['open']
    return None


def closed_today_line(records, d, name_key='name', hours_key='hours'):
    """Build the per-day 'what is closed today' line for the itinerary.

    records: iterable of dicts. Returns a list of names shut on date d.
    """
    shut = []
    for r in records:
        if is_open_on(r.get(hours_key, ''), d) is False:
            shut.append(r.get(name_key, '?'))
    return sorted(shut)


def for_note(spec, max_len=90):
    """Render hours for the Google Maps note field: normalized, CLOSED in caps,
    truncated on a separator rather than mid-token."""
    s = normalize(spec)
    s = re.sub(r'\bclosed\b', 'CLOSED', s, flags=re.I)
    if len(s) <= max_len:
        return s
    cut = s[:max_len]
    for sep in ('; ', ', '):
        if sep in cut:
            return cut[:cut.rfind(sep)] + '; ...'
    return cut.rstrip() + '...'


# ---------------------------------------------------------------- self-test

if __name__ == '__main__':
    CASES = [
        'daily 09:00-18:00',
        'M-F 09:00-17:00; CLOSED Sa Su',
        'Tu-Su 10:00-17:00 (last entry 16:30); CLOSED M',
        'Tu-Sa 11:30-14:00, 17:30-22:00 (LO 21:00); CLOSED Su M',
        'W-M 10:00-18:00; CLOSED Tu; CLOSED 3rd Wed',
        'daily 06:00-18:00',
        '24h',
        'always open',
        'by appointment',
        'unknown, verify',
        'M-Th 09:00-16:00; CLOSED F Sa Su',
        # forms documented in references/hours-and-closures.md
        'M-Th 9-4; CLOSED F-Su',
        '9-18 (last entry -60m)',
        'Apr-Oct 9-18; Nov-Mar 10-16, CLOSED W',
        'CLOSED M (+Tu if M is holiday); 9-17',
        'M-Su 9-17; CLOSED 3rd-W (monthly maintenance)',
        'Su-Th 24h; F-Sa 06:00-02:00',
        'Tu-Sa 11:30-14:00, 18:00-22:00 (LO 21:30); CLOSED M, Su',
        'by appointment only; CLOSED M',
    ]
    print('%-58s %-6s %s' % ('SPEC', 'PROBS', 'NORMALIZED'))
    for c in CASES:
        pr = validate(c)
        print('%-58s %-6d %s' % (c[:56], len(pr), normalize(c)))
        for x in pr:
            print('      ! %s' % x)
    print()
    print('closed_days(Tu-Su ...; CLOSED M) ->',
          sorted(closed_days('Tu-Su 10:00-17:00; CLOSED M')))
    print('is_open_on Mon 2026-07-20 ->',
          is_open_on('Tu-Su 10:00-17:00; CLOSED M', _date(2026, 7, 20)))
    print('is_open_on Tue 2026-07-21 ->',
          is_open_on('Tu-Su 10:00-17:00; CLOSED M', _date(2026, 7, 21)))
    print('for_note ->', for_note('Tu-Sa 11:30-14:00, 17:30-22:00 (LO 21:00); CLOSED Su M'))
    print()
    print('--- negative cases (each should report a problem) ---')
    for bad in ['M-R 9-4', 'Tu-Su 10am-5pm', '', 'M-F 9:00—17:00', 'daily 18:00-09:00']:
        print('%-24r %s' % (bad, validate(bad)))
