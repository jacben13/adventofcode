from aoc_modules import aoc_library
from itertools import product
from collections import Counter


puzzle = aoc_library.read_2d('input.txt', convert_to_int=True)
h = len(puzzle)
w = len(puzzle[0])

for r in puzzle:
    print(r)


def neighbors(i, j):
    dydxs = product([-1, 0, 1], repeat=2)
    coords = ((dy + i, dx + j) for (dy, dx) in dydxs)
    return list([c for c in coords if 0 <= c[0] < h and 0 <= c[1] < w])


def octo_flash(octopi, f, r, c):
    if (r, c) in f:
        return
    f.add((r, c))
    for y, x in neighbors(r, c):
        octopi[y][x] += 1
        if octopi[y][x] > 9 and (y, x) not in f:
            octo_flash(octopi, f, y, x)


sync = False
steps = 0
flashes = 0
octopi_num = h * w

while not sync:
    # Increment all octopi by 1
    for i, r in enumerate(puzzle):
        for j, o in enumerate(r):
            puzzle[i][j] += 1

    # Find all octopi that are flashing from regular growth
    flashers = set()
    for r, row in enumerate(puzzle):
        for c, octopus in enumerate(row):
            if octopus > 9:
                octo_flash(puzzle, flashers, r, c)

    # Check if
    # For all octopi that flashed, reset to 0
    for i, j in flashers:
        puzzle[i][j] = 0
    flashes += len(flashers)
    if len(flashers) >= octopi_num:
        sync = True
    steps += 1

print(steps)

