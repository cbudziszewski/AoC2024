#!/usr/bin/env python3
import numpy as np


def find_xmas(matrix,r,c,h,w):
    print(f"{r} {c} {h} {w}")

    L = []

    if r-1 >=0 and r+1 < h and c-1 >= 0 and c+1 < w:
        L.append(''.join([matrix[r-1,c-1], matrix[r,c], matrix[r+1,c+1]]))
        L.append(''.join([matrix[r+1,c-1], matrix[r,c], matrix[r-1,c+1]]))
        L.append(''.join([matrix[r+1,c+1], matrix[r,c], matrix[r-1,c-1]]))
        L.append(''.join([matrix[r-1,c+1], matrix[r,c], matrix[r+1,c-1]]))

    print(L)
    b = [ l == 'MAS' for l in L ]
    print(f"count: {sum(b)}")

    return sum(b) == 2

with open('input.txt') as f:
    matrix = np.array([ list(line.rstrip()) for line in f if len(line) > 1])

h = len(matrix)
w = len(matrix[0])
find_xmas(matrix,0,0,h,w)
find_xmas(matrix,0,w-1,h,w)
find_xmas(matrix,h-1,0,h,w)
find_xmas(matrix,h-1,w-1,h,w)


s = 0
for y, r in enumerate(matrix):
    for x, c in enumerate(r):
        if c == 'A':
            s = s + find_xmas(matrix,y,x,w,h)
print(f"Total X-MAS: {s}")



