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

done = False
best = 0
speed = 0
target_t = 0
while speed < abs(min(y_range)):
    possible = True
    t = 1
    while possible:
        _, y = get_pos(0, speed, t)
        if y in y_range:
            break
        elif y < min(y_range):
            possible = False
            break
        t += 1
    if possible and speed > best:
        best = speed
        target_t = t
    speed += 1


# current_y = vy0 * current_time - (current_time - 1) * (current_time) // 2
height = best * best - (best - 1) * (best) // 2
print(f'Best Y: {best}')
print(f'Height reached: {height}')