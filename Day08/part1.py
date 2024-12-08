#!/usr/bin/env python3
from collections import defaultdict
from numpy import array, ndenumerate

with open('example.txt') as file:
    city =  array([ list(line.rstrip()) for line in file if len(line) > 1])


print(city)

antinodes = defaultdict(list)
antennas = defaultdict(list)


for idx, x in ndenumerate(city):
    if x not in ['.']:
        antennas[x].append(idx)


print(antennas)





