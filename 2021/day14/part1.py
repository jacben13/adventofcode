from aoc_modules import aoc_library
from itertools import product
from collections import Counter, defaultdict


puzzle = aoc_library.read_input('input.txt')

polymer = puzzle[0]
rules = defaultdict(lambda: '')
for rule in puzzle:
    if '->' in rule:
        a, b = rule.replace(' ', '').split('->')
        rules[a] = b

print(polymer)

for x in range(10):
    new_polymer = ''
    for i, f in enumerate(polymer):
        fragment = f
        p = ''
        if i < len(polymer) - 1:
            p = polymer[i:i+2]
        fragment += rules[p]
        new_polymer += fragment
    polymer = new_polymer

print(len(polymer))
poly_count = Counter(polymer)
print(poly_count.most_common()[0][1] - poly_count.most_common()[-1][1])