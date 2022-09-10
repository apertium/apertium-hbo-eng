#!/usr/bin/env python3

import sys

for line in sys.stdin:
    if not line.strip():
        continue
    if '<sent>' in line:
        print(line.strip())
    else:
        print(line.strip(), end=' ')
print('')
