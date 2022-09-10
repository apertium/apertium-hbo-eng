#!/usr/bin/env python3

import glob
from collections import defaultdict
import sys

POS_table = {
    'ADP': 'pr',
    'CCONJ': 'cnjcoo',
    'NOUN': 'n',
    'PROPN': 'np',
    'PUNCT': 'sent',
    'VERB': 'v',
}

FEAT_table = [
    ('HebBinyan=PAAL', 'actv'),
    ('Aspect=Perf', 'perf'),
    ('Person=1', 'p1'),
    ('Person=2', 'p2'),
    ('Person=3', 'p3'),
    ('Gender=Fem', 'f'),
    ('Gender=Masc', 'm'),
    ('Number=Plur', 'pl'),
    ('Number=Sing', 'sg'),
    ('PronType=Art', 'def'),
]

FEAT_SKIP = ['Mood=Ind', 'VerbForm=Fin']

def line_to_ana(line):
    ls = line.strip().split('\t')
    if len(ls) != 10:
        return ('', '')
    surf = ls[1]
    lem = ls[2].strip('_') or surf
    tagls = [POS_table.get(ls[3], ls[3].lower())]
    feats = sorted(ls[5].strip('_').split('|'))
    for ud, ap in FEAT_table:
        if ud in feats:
            feats.remove(ud)
            tagls.append(ap)
    for feat in feats:
        if not feat or feat in FEAT_SKIP:
            continue
        tagls.append(feat)
    tagls.append('@'+ls[7])
    tagls.append(f'#{ls[0]}→{ls[6]}')
    tags = ''.join(f'<{t}>' for t in tagls)
    return (surf, lem+tags)

for line in sys.stdin:
    if not line.strip():
        print('')
        continue
    ls = line.strip().split('\t')
    if len(ls) != 10:
        continue
    elif '-' in ls[0]:
        continue
    surf, ana = line_to_ana(line)
    print(f'^{surf}/{ana}$', end=' ')
