from aoc_modules import aoc_library
from itertools import product
from collections import Counter, defaultdict, deque
import re


def get_pos(vx0, vy0, current_time):
    current_y = vy0 * current_time - (current_time - 1) * (current_time) // 2

    # ignore -ve x as the input is to the right
    current_x = (
        (2 * vx0 - current_time + 1) * (current_time) // 2
    if current_time < vx0
        else vx0 * (vx0 + 1) // 2
    )

    return current_x, current_y


puzzle = aoc_library.read_input('input.txt')
puzzle = puzzle[0]

print(puzzle)

m = re.findall(r'[x|y]=-?\d*\.\.-?\d*', puzzle)
x_range = []
for s in m:
    axis = s[0]
    target = s[2:].split('..')
    if axis == 'x':
        x_range = range(int(target[0]), int(target[1]) + 1)
    elif axis == 'y':
        y_range = range(int(target[0]), int(target[1]) + 1)

print(x_range)
print(y_range)

speed = min(y_range) - 1
target_t = 0
y_speeds = set()
while speed < abs(min(y_range)):
    possible = True
    t = 1
    while possible:
        _, y = get_pos(0, speed, t)
        if y in y_range:
            y_speeds.add((speed, t))
        elif y < min(y_range):
            possible = False
        t += 1
    speed += 1

valid_combos = set()
for y, t in y_speeds:
    for x in range(max(x_range), 0, -1):
        x_pos, _ = get_pos(x, y, t)
        if x_pos in x_range:
            valid_combos.add((x, y))

print(f'Good velocities: {len(valid_combos)}')
print(valid_combos)
# print(y_speeds)
# print(len(y_speeds))