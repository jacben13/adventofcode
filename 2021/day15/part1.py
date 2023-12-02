from aoc_modules import aoc_library
from itertools import product
from collections import Counter, defaultdict, deque


puzzle = aoc_library.read_2d('input.txt', convert_to_int=True)

print(puzzle)
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
unvisited = set()
shortest_path = defaultdict(lambda: float('inf'))
shortest_path[start] = 0
previous_nodes = {}

for j, row in enumerate(puzzle):
    for i, col in enumerate(row):
        unvisited.add((i, j))

while unvisited:
    current_min_node = None
    for node in unvisited:
        if not current_min_node:
            current_min_node = node
        elif shortest_path[node] < shortest_path[current_min_node]:
            current_min_node = node

    neighbor_list = neighbors(current_min_node)
    for neighbor in neighbor_list:
        tentative_value = shortest_path[current_min_node] + puzzle[neighbor[1]][neighbor[0]]
        if tentative_value < shortest_path[neighbor]:
            shortest_path[neighbor] = tentative_value
            previous_nodes[neighbor] = current_min_node

    unvisited.remove(current_min_node)

print(shortest_path[h - 1, w - 1])