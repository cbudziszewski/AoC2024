#!/usr/bin/env python3
import re

with open('input.txt') as f:
    listofpairs = [ re.findall(r'\d+', line) for line in f ]
a = [ int(a) for (a, b) in listofpairs ]
b = [ int(b) for (a, b) in listofpairs ]

multmap = dict()

for i in b:
    if i in multmap.keys():
        multmap[i] += 1
    else:
        multmap[i] = 1

d = sum([ x * multmap[x] for x in a if x in multmap.keys()])

print(d)

