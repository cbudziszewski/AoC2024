#!/usr/bin/env python3

from collections import defaultdict

da_rulez=defaultdict(list)
simple_rulez=[]
updates=[]

with open('input.txt') as file:
    part = 1
    for line in file:
        if not line.rstrip():
            part = part +1
            continue
        if part == 1:
            k,v = line.rstrip().split('|')
            da_rulez[k].append(v)
            simple_rulez.append((k,v))
        if part == 2: 
            updates.append(line.rstrip().split(','))

def middle_value(update, rulez):
    middle = 0
    for idx, num in enumerate(update):
        prefix = update[:idx]
        pivot = update[idx]
        suffix = update[idx+1:]
        if len(prefix) == len(suffix):
            print(f"middle {num} {pivot}")
            middle = int(pivot)

        print(f"idx: {idx} Prefix {prefix} pivot {pivot} suffix {suffix}")
        if not all([f in da_rulez[num] for f in suffix]):
            return 0

    return middle

sum_of_middles = 0
for u in updates:
    sum_of_middles = sum_of_middles + middle_value(u,da_rulez)

print(f"Sum of Middles: {sum_of_middles}")



