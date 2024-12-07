#!/usr/bin/env python3
calibrations = dict()
with open('example.txt') as file:
    for line in file:
        k, v = line.rstrip().split(":")
        calibrations[int(k)] = list(map(int,v.split()))
        print(calibrations)

