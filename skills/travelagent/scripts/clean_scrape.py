# -*- coding: utf-8 -*-
"""De-boilerplate raw scrape dumps.

    py clean_scrape.py <scrape dir> [--marker "Read Full Review"]

Reads  <scrape dir>/raw/*.txt
Writes <scrape dir>/clean/*.txt

Steps, in order (see references/scraping-playbook.md):
  1. unescape literal \\n sequences that `agent-browser eval` returns
  2. drop boilerplate lines (nav, subscribe prompts, footer legal, cookie text)
  3. drop ALL-CAPS lines under 40 chars (section labels and nav)
  4. dedupe paragraphs by exact match, preserving first-seen order

Expect roughly a 90 percent size reduction. If --marker is given, the per-file
count of that marker is printed before and after so you can confirm the scroll
passes captured every item and cleaning did not eat any.
"""
import os
import re
import sys
import glob

BOILER = [
    'Skip to main content', 'Sign In', 'Sign Up', 'Subscribe', 'Newsletter',
    'Read More', 'Read Full Review', 'Advertisement', 'Sponsored',
    'Share on Facebook', 'Share on Twitter', 'Share on Pinterest',
    'Follow us', 'Terms of Use', 'Privacy Policy', 'Cookie', 'Cookies',
    'Your Privacy Choices', 'User Agreement', 'All rights reserved',
    'Conde Nast', 'Condé Nast', 'Ad Choices', 'Accessibility Help',
    'Do Not Sell', 'Site Map', 'Contact the Editors', 'Careers',
    'Sign up for our newsletter', 'Get the newsletter', 'Most Popular',
    'More From', 'Related Stories', 'You Might Also Like', 'Trending',
    'Load More', 'Show more', 'Continue reading', 'Log in',
    'Manage Preferences', 'Accept All', 'Reject All',
    'Enable JavaScript', 'Please enable', 'Something went wrong',
    'By clicking', 'We and our partners',
]
# lines that are ONLY these are dropped; substrings above are matched loosely
BOILER_LOW = [b.lower() for b in BOILER]

DROP_PATTERNS = [
    re.compile(r'^\s*$'),
    re.compile(r'^\W{0,3}$'),                       # lone punctuation
    re.compile(r'^\d+\s*/\s*\d+$'),                 # slide counters "3 / 25"
    re.compile(r'^(next|prev|previous|back|close|menu|search)$', re.I),
    re.compile(r'^photo(graph)?s?\s*(by|:)', re.I),  # photo credits
    re.compile(r'^courtesy of', re.I),
    re.compile(r'^\$\d+\s*$'),                      # bare price chips
]


def looks_boiler(line):
    low = line.strip().lower()
    if not low:
        return True
    for b in BOILER_LOW:
        if low == b or (len(low) < 70 and b in low):
            return True
    for p in DROP_PATTERNS:
        if p.match(line.strip()):
            return True
    s = line.strip()
    if len(s) < 40 and s.isupper() and any(c.isalpha() for c in s):
        return True
    return False


def clean_text(raw):
    txt = raw.replace('\\n', '\n').replace('\\t', '\t').replace('\\"', '"')
    lines = [l.rstrip() for l in txt.split('\n')]
    kept, seen = [], set()
    for l in lines:
        if looks_boiler(l):
            continue
        key = re.sub(r'\s+', ' ', l.strip().lower())
        if len(key) > 25:
            if key in seen:
                continue
            seen.add(key)
        kept.append(l.strip())
    # collapse runs of blank lines
    out, blank = [], False
    for l in kept:
        if not l:
            if blank:
                continue
            blank = True
        else:
            blank = False
        out.append(l)
    return '\n'.join(out).strip() + '\n'


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 0
    base = sys.argv[1]
    marker = None
    if '--marker' in sys.argv:
        marker = sys.argv[sys.argv.index('--marker') + 1]
    raw_dir = os.path.join(base, 'raw')
    clean_dir = os.path.join(base, 'clean')
    os.makedirs(clean_dir, exist_ok=True)

    files = sorted(glob.glob(os.path.join(raw_dir, '*.txt')))
    if not files:
        print('no raw/*.txt under %s' % base)
        return 1
    tin = tout = 0
    hdr = '%-34s %10s %10s %6s' % ('FILE', 'RAW', 'CLEAN', 'KEPT%')
    if marker:
        hdr += '  %s' % marker[:18]
    print(hdr)
    print('-' * (len(hdr) + 2))
    for p in files:
        raw = open(p, encoding='utf-8', errors='replace').read()
        cl = clean_text(raw)
        outp = os.path.join(clean_dir, os.path.basename(p))
        with open(outp, 'w', encoding='utf-8') as f:
            f.write(cl)
        tin += len(raw)
        tout += len(cl)
        line = '%-34s %10d %10d %5.1f%%' % (
            os.path.basename(p)[:34], len(raw), len(cl),
            100.0 * len(cl) / max(len(raw), 1))
        if marker:
            line += '  %d -> %d' % (raw.count(marker), cl.count(marker))
        print(line)
    print('-' * (len(hdr) + 2))
    print('%-34s %10d %10d %5.1f%%' % ('TOTAL', tin, tout,
                                       100.0 * tout / max(tin, 1)))
    if marker:
        print('\nNote: %r is in the boilerplate drop list, so a 0 after cleaning '
              'is expected. Use the RAW count to confirm scroll coverage.' % marker)
    return 0


if __name__ == '__main__':
    sys.exit(main())
