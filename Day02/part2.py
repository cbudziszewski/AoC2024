#!/usr/bin/env python3
import re

def is_safe(levels):
    diffs = [ a[0]-a[1] for a in zip(levels[:-1], levels[1:])]

    return all([ a >= 1 and a <= 3 for a in diffs]) or \
            all([ a <= -1 and a >= -3 for a  in diffs])

def is_safe_tolerate(levels):
    ''' brute force approach again '''
    safe = is_safe(levels)
    t = 0

    while (not safe) and (t < len(levels)):
        copy = levels.copy()
        del copy[t]
        safe = is_safe(copy)
        t = t +1

    return safe


with open('input.txt') as file:
    listofreports = [list(map(int, re.findall(r'\d+', line))) for line in file ]

safe = sum([is_safe_tolerate(report) for report in listofreports])

print(safe)





