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

ps = defaultdict(lambda: 0)
for i, _ in enumerate(polymer):
    if i < len(polymer) - 1:
        t = polymer[i:i+2]
        if len(t) > 1:
            ps[t] += 1

polymer = ps
print(polymer)
print(rules)

for _ in range(40):
    new_polymer = polymer.copy()
    for pair, count in polymer.items():
        if pair in rules:
            new_polymer[pair] -= count
            new_char = rules[pair]
            new_polymer[pair[0] + new_char] += count
            new_polymer[new_char + pair[1]] += count
    polymer = new_polymer

new_counter = defaultdict(lambda: 0)
for k, v in polymer.items():
    new_counter[k[0]] += v
    new_counter[k[1]] += v
    # print(f'{k[0]}: {v}')

new_counter[puzzle[0][-1]] += 1
new_counter[puzzle[0][0]] += 1
ans_counts = [c[1] // 2 for c in new_counter.items()]
print(polymer)
print(ans_counts)
print(max(ans_counts) - min(ans_counts))