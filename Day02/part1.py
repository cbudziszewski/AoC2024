#!/usr/bin/env python3
import re

with open('input.txt') as f:
    listofreports = [ re.findall(r'\d+', line) for line in f ]


safecounter=0
for level in listofreports:
    leveldiff = [ int(a[0])-int(a[1]) for a in zip(level[:-1], level[1:])]

    if all([a > 0 for a in leveldiff]) and all([a <= 3 for a in leveldiff]) \
        or all([a < 0 for a in leveldiff]) and all([a >= -3 for a in leveldiff]):
        safecounter = safecounter + 1

print(safecounter)




