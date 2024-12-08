#!/usr/bin/env python3
from collections import defaultdict
from numpy import array, ndenumerate
from itertools import product

with open('input.txt') as file:
    city =  array([ list(line.rstrip()) for line in file if len(line) > 1])


print(city)
print(f"city shape {city.shape}")


def antinodes(antenna_list, shape):
    _antinodes = set()
    for a, b in product(antenna_list, repeat=2):
        # skip same
        if a == b: 
            continue
        # skip doubles: (a, b) == (b, a)
        if a[0] > b[0]:
            continue
        dx, dy = a[0] - b[0], a[1] - b[1]
        if (0 <= a[0] + dx < shape[0]) and (0 <= a[1] + dy < shape[1]):
            _antinodes.add((a[0] + dx, a[1] + dy))
        if (0 <= b[0] - dx < shape[0]) and (0 <= b[1] - dy < shape[1]):
            _antinodes.add((b[0] - dx, b[1] - dy))

        print(f"Pair: {a} {b}, (dx,dy)=({dx},{dy}), AN: {_antinodes}")
    return _antinodes

antennas = defaultdict(list)
all_antenna_locations = set()
for idx, x in ndenumerate(city):
    if x not in ['.']:
        antennas[x].append(idx)
        all_antenna_locations.add(idx)
print(antennas)

an = set()
for freq in antennas.keys():
    an.update(antinodes(antennas[freq],city.shape))
    print(f"update: {an}")

print(f"Antinodes: {an}")
print(f"Antinode count: {len(an)}")


