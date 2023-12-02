from aoc_modules import aoc_library
from collections import Counter


puzzle = aoc_library.read_input('input.txt')

scoring = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

openers = ['(', '[', '{', '<']
closers = list(scoring.keys())
pairs = {')':'(', ']':'[', '}':'{', '>':'<'}

illegal = []
incomplete = []
for line in puzzle:
    open_chunks = []
    for c in line:
        if c in openers:
            open_chunks.append(c)
        elif c in closers and open_chunks[-1] != pairs[c]:
            illegal.append(c)
            break
        elif c in closers and open_chunks[-1] == pairs[c]:
            open_chunks.pop()
    else:
        incomplete.append(line)

ans = 0
for i in illegal:
    ans += scoring[i]
print(ans)