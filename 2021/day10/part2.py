from aoc_modules import aoc_library
from collections import Counter


puzzle = aoc_library.read_input('input.txt')

scoring = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

def score(added_chars):
    ans = 0
    for c in added_chars:
        ans *= 5
        ans += scoring[c]
    return ans

openers = ['(', '[', '{', '<']
closers = list(scoring.keys())
pairs = {')': '(', ']': '[', '}': '{', '>': '<',
         '(': ')', '[': ']', '{': '}', '<': '>'}

incomplete_scores = []
for line in puzzle:
    open_chunks = []
    for c in line:
        if c in openers:
            open_chunks.append(c)
        elif c in closers and open_chunks[-1] != pairs[c]:
            break
        elif c in closers and open_chunks[-1] == pairs[c]:
            open_chunks.pop()
    else:
        added = []
        for a in open_chunks[::-1]:
            added.append(pairs[a])
        print(added)
        print(score(added))
        incomplete_scores.append(score(added))


incomplete_scores.sort()
print(incomplete_scores[len(incomplete_scores) // 2])
