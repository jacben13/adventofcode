from aoc_modules import aoc_library
from itertools import product
from collections import Counter, deque, defaultdict
from string import ascii_lowercase



puzzle = aoc_library.read_input('input.txt')


caves = defaultdict(list)
for line in puzzle:
    origin, destination = line.split('-')
    caves[origin].append(destination)
    if origin != 'start':
        caves[destination].append(origin)


# # Remove any deadend small caves, that is a small cave that is only connected to one other small cave
# # Also remove connections to the start cave
# to_remove = []
# for c, v in caves.items():
#     if len(v.connections) == 1 and v.connections.issubset(set(ascii_lowercase)):
#         to_remove.append(c)

# print(f'Removed the following caves: {to_remove}')
# for r in to_remove:
#     for c in caves.values():
#         c.connections.discard(r)
#         c.connections.discard('start')
#     caves.pop(r)

for k, v in caves.items():
    print(f'{k} -> {v}')


ans = 0
start = ('start', set(['start']))
d = deque([start])
while d:
    pos, small = d.popleft()
    if pos == 'end':
        ans += 1
        continue
    for c in caves[pos]:
        if c not in small:
            new_small = set(small)
            if c.islower():
                new_small.add(c)
            d.append((c, new_small))

print(ans)



# Path generation
# Start at start, iterate for each choice available
# update current pos, add cave to seen set
# if at end, add path
# if nowhere left to go, break