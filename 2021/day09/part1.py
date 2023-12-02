from aoc_modules import aoc_library
from collections import Counter


puzzle = aoc_library.read_input('input.txt')

heights = []
for l in puzzle:
    h = []
    for n in l:
        h.append(int(n))
    heights.append(h)

sum_of_lows = 0
coords_of_lows = []
for r, row in enumerate(heights):
    for c, col in enumerate(row):
        neighbors = []
        if c > 0:
            neighbors.append(heights[r][c-1])
        if c + 1< len(row):
            neighbors.append(heights[r][c+1])
        if r > 0:
            neighbors.append(heights[r-1][c])
        if r + 1 < len(heights):
            neighbors.append(heights[r+1][c])
        if min(neighbors) > col:
            sum_of_lows += col + 1
            coords_of_lows.append([r, c])

print(sum_of_lows)