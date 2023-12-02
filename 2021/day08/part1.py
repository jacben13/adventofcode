from aoc_modules import aoc_library
from collections import Counter


puzzle = aoc_library.read_input('input.txt')

outputs = []
inputs = []
for p in puzzle:
    inputs.append(p.split('|')[0].split())
    outputs.append(p.split('|')[1].split())

output_counter = Counter()
for o in outputs:
    for p in o:
        output_counter.update([len(p)])

print(output_counter)
# 2 segments: 1, 4 segments: 4, 3 segments: 7, 7 segments: 8
ans = output_counter[2] + output_counter[4] + output_counter[3] + output_counter[7]
print(f'Sum of 1, 4, 7, 8: {ans}')