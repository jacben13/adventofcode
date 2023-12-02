from aoc_modules import aoc_library
from itertools import product
from collections import Counter, defaultdict, deque
import copy
import heapq


puzzle = aoc_library.read_2d('input.txt', convert_to_int=True)

new_puzzle = copy.deepcopy(puzzle)

for r in range(1, 5):
    for y, row in enumerate(puzzle):
        for n in row:
            new_val = n + (1 * r)
            new_val = new_val if new_val <= 9 else new_val % 9
            new_puzzle[y].append(new_val)

puzzle = copy.deepcopy(new_puzzle)

for r in range(1, 5):
    for row in puzzle:
        new_row = []
        for n in row:
            new_val = n + (1 * r)
            new_val = new_val if new_val <= 9 else new_val % 9
            new_row.append(new_val)
        new_puzzle.append(new_row)

puzzle = new_puzzle

h = len(puzzle)
w = len(puzzle[0])


def neighbors(t):
    i, j = t
    n = []
    if i < w - 1:
        n.append((i + 1, j))
    if i > 0:
        n.append((i - 1, j))
    if j < h - 1:
        n.append((i, j + 1))
    if j > 0:
        n.append((i, j - 1))
    return n


start = (0, 0)
goal = (w - 1, h - 1)
shortest_path = defaultdict(lambda: float('inf'))
shortest_path[start] = 0
queue = []
heapq.heappush(queue, (0, 0))

while True:
    x0, y0 = heapq.heappop(queue)
    cost = shortest_path[(x0, y0)]
    if x0 == w - 1 and y0 == h - 1:
        break
    for neighbor in neighbors((x0, y0)):
        cost_to_neighbor = cost + puzzle[neighbor[1]][neighbor[0]]
        if cost_to_neighbor < shortest_path[neighbor]:
            shortest_path[neighbor] = cost_to_neighbor
            heapq.heappush(queue, neighbor)

print(shortest_path[h - 1, w - 1])