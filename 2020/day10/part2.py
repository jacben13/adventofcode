from aoc_modules import aoc_library
import itertools
import math

puzzle_input = aoc_library.read_numbers('test_input.txt')
puzzle_input.sort()

DEVICE_MAX_JOLTS = max(puzzle_input) + 3
SOCKET = 0
puzzle_input.insert(0, SOCKET)
puzzle_input.append(DEVICE_MAX_JOLTS)


def row_delta(n, puzzle_input):
    return puzzle_input[n+1] - puzzle_input[n]


def check_adapter_chain(adapters):
    for a in range(1, len(adapters)):
        if row_delta(a, adapters) > 3:
            return False
    print(adapters)
    return True


def calculate_n_combos(n ,r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


valid_combos = 0


required_adapter_chains = []
number_added = []
print(puzzle_input)
for i in range(0, len(puzzle_input) - 1):
    if puzzle_input[i] in number_added:
        continue
    candidate_chain = []
    d = 0
    j = i
    while d < 3:
        d = row_delta(j, puzzle_input)
        candidate_chain.append(puzzle_input[j])
        number_added.append(puzzle_input[j])
        j += 1
    required_adapter_chains.append(candidate_chain)

print(required_adapter_chains)

