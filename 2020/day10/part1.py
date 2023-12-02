from aoc_modules import aoc_library

puzzle_input = aoc_library.read_numbers('input.txt')
puzzle_input.sort()


def row_delta(n, puzzle_input):
    return puzzle_input[n] - puzzle_input[n-1]


device_max_jolts = max(puzzle_input) + 3
socket = 0

puzzle_input.append(device_max_jolts)
puzzle_input.insert(0, socket)

deltas = {}
for i in range(len(puzzle_input)):
    d = 0
    if i == 0:
        continue
    else:
        d = row_delta(i, puzzle_input)

    print('d: {} at {}'.format(d, i))
    if d in deltas.keys():
        deltas[d] += 1
    else:
        deltas[d] = 1

print(deltas)
print('Multiply: {}'.format(deltas[1] * deltas[3]))