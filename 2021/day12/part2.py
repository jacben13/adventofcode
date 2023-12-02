from aoc_modules import aoc_library
from itertools import product
from collections import Counter, deque, defaultdict
from string import ascii_lowercase


puzzle = aoc_library.read_input('input.txt')

caves = defaultdict(list)
for line in puzzle:
    origin, destination = line.split('-')
    if destination != 'start':
        caves[origin].append(destination)
    if origin != 'start':
        caves[destination].append(origin)

caves.pop('end')
for k, v in caves.items():
    print(f'{k} -> {v}')

ans = 0
start = ('start', set(['start']), False)
d = deque([start])
while d:
    pos, small, twice = d.popleft()
    if pos == 'end':
        ans += 1
        continue
    for c in caves[pos]:
        if c not in small:
            new_small = set(small)
            if c.islower():
                new_small.add(c)
            d.append((c, new_small, twice))
        elif c in small and not twice and c not in ['start', 'end']:
            d.append((c, small, True))

print(ans)



# Path generation
# Start at start, iterate for each choice available
# update current pos, add cave to seen set
# if at end, add path
# if nowhere left to go, break