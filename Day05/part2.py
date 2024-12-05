#!/usr/bin/env python3

from collections import defaultdict

da_rulez=defaultdict(list)
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
        if part == 2: 
            updates.append(line.rstrip().split(','))

def is_correct(update, rulez):
    for idx, num in enumerate(update):
        prefix = update[:idx]
        pivot = update[idx]
        suffix = update[idx+1:]
        if not all([f in da_rulez[num] for f in suffix]):
            return False
    return True

def get_correct_middle(update, rulez):
    print(f"incorrect update: {update}")
    middle = int((len(update))/2)+1

    for i in range(0, middle):
        # get all elements that are "right of" another element
        subset = [ e for num in update for e in rulez[num] ]
        # get the left most element
        single = [ num for num in update if num not in subset ]
        print(f"update {update}\nsubset {subset}\nsingle {single}")
        update.remove(single[0])
    return int(single[0])


sum_of_middles = 0
for u in updates:
    if not is_correct(u, da_rulez):
       sum_of_middles = sum_of_middles + get_correct_middle(u, da_rulez)

print(f"Sum of Middles: {sum_of_middles}")



