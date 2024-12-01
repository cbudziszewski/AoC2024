#!/usr/bin/env python3
import re

with open('input.txt') as f:
    listofpairs = [ re.findall(r'\d+', line) for line in f ]

print(listofpairs)


a = [ int(a) for (a, b) in listofpairs ]
b = [ int(b) for (a, b) in listofpairs ]
a.sort()
b.sort()
d = [ abs(x - y) for (x, y) in zip(a, b)]

print(sum(d))
