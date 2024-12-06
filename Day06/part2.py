#!/usr/bin/env python3
from numpy import array
from collections import namedtuple
from dataclasses import dataclass, replace
from copy import deepcopy

@dataclass
class Guard:
    x: int
    y: int
    direction: str
    visited: list

def turn(g):
    t = {}
    t['^'] = '>'
    t['>'] = 'v'
    t['v'] = '<'
    t['<'] = '^'
    g.direction = t[g.direction]

def next_is_obstacle(g, m):
    return (g.direction == '>' and  m[g.y][g.x+1] in ['#', 'O']) \
        or (g.direction == '<' and  m[g.y][g.x-1] in ['#', 'O']) \
        or (g.direction == 'v' and  m[g.y+1][g.x] in ['#', 'O']) \
        or (g.direction == '^' and  m[g.y-1][g.x] in ['#', 'O'])

def next_is_outofbounds(g, w, h):
    return (g.direction == '>' and g.x+1 >= w) \
        or (g.direction == '<' and g.x-1 < 0 ) \
        or (g.direction == '^' and g.y-1 < 0 ) \
        or (g.direction == 'v' and g.y+1 >= h) 

def move(g):
    g.x = g.x + 1 if g.direction == '>' else g.x
    g.x = g.x - 1 if g.direction == '<' else g.x
    g.y = g.y + 1 if g.direction == 'v' else g.y
    g.y = g.y - 1 if g.direction == '^' else g.y

def is_stuck_in_a_loop(m, g):
    while True:
        if next_is_outofbounds(g, m.shape[1], m.shape[0]):
#            print("OUT")
            return False
        elif next_is_obstacle(g, m): 
#            print("TURN")
            turn(g)
        else:
#            print("MOVE")
            move(g)

        update = (g.x, g.y, g.direction)
        if update in g.visited:
#            print("LOOP")
            return True
        g.visited.add(update)

with open('input.txt') as f:
    matrix = array([ list(line.rstrip()) for line in f if len(line) > 1])

for y in range(0,matrix.shape[0]):
    for x in range(0,matrix.shape[1]):
        if matrix[y][x] == '^':
            initial_x = x
            initial_y = y

# record the initial path of the guard.
guard = Guard(initial_x, initial_y, '^', {(initial_x, initial_y, '^')})
print(f"initial guard {guard}")
#print(matrix)
is_stuck_in_a_loop(matrix, guard)
print(f"visited: {guard.visited}")

# idea: put obstacle in each location on the path and see if we can escape or reach the starting point.
# it is enough to start right before each obstacle. 
# (3,3,^) and (3,3,>) are different visited places.

testpositions = set()
for v in guard.visited:
    testpositions.add((v[0],v[1]))

print(f"unique obstacle positions: {len(testpositions)}, Path length: {len(guard.visited)}")

l = []
for pos in testpositions:
    mc = deepcopy(matrix)
    mc[pos[1],pos[0]] = 'O'
#    print(mc)
    gc = Guard(x=initial_x, y=initial_y, direction='^',visited={(initial_x, initial_y, '^')})
#    print(gc)
    l.append( is_stuck_in_a_loop(mc,gc) )

print(f"is stuck in a loop {sum(l)} times")


