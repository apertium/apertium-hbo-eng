#!/usr/bin/env python3

import sys

in_lu = False
in_sl = False
esc = False
for c in sys.stdin:
    sys.stdout.write(c)
    if esc:
        esc = False
    elif not esc and c == '\\':
        esc = True
    elif not in_lu and c == '^':
        in_lu = True
        in_sl = True
    elif in_lu and c == '/':
        in_sl = False
    elif in_lu and c == '$':
        in_lu = False
    elif in_sl and c == '<':
        sys.stdout.write('sl:')
