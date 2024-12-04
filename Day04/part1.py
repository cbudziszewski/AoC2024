#!/usr/bin/env python3
import numpy as np


def find_xmas(matrix,r,c,h,w):
#    print(matrix[r-3:r+4,c-3:c+4])
    print(f"{r} {c} {h} {w}")

    L = []

    if r+4 <= h:
        L.append(''.join(matrix[r:r+4,c]))
    if r-3 >= 0 and r+1 <= h :
        L.append(''.join(matrix[r-3:r+1,c][::-1]))
    if c+4 <= w:
        L.append(''.join(matrix[r,c:c+4]))
    if c-3 >= 0 and c+1 <= w:
        L.append(''.join(matrix[r,c-3:c+1][::-1]))
    if r-3 >= 0 and c-3 >= 0:
        L.append(''.join([matrix[r,c], matrix[r-1,c-1], matrix[r-2,c-2], matrix[r-3, c-3]]))
    if r-3 >= 0 and c+3 < w:
        L.append(''.join([matrix[r,c], matrix[r-1,c+1], matrix[r-2,c+2], matrix[r-3, c+3]]))
    if r+3 < h and c-3 >= 0:
        L.append(''.join([matrix[r,c], matrix[r+1,c-1], matrix[r+2,c-2], matrix[r+3, c-3]]))
    if r+3 < h and c+3 < w:
        L.append(''.join([matrix[r,c], matrix[r+1,c+1], matrix[r+2,c+2], matrix[r+3, c+3]]))

    print(L)
    b = [ l == 'XMAS' for l in L ]
    print(f"count: {sum(b)}")

    return sum(b)

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
        if c == 'X':
            s = s + find_xmas(matrix,y,x,w,h)
print(f"Total XMAS: {s}")



