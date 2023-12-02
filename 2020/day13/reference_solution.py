from aoc_modules import aoc_library

def part2_alt(bus_ids, remainders):
    t, step = 0,1
    for m,d in zip(bus_ids, remainders):
        while (t+d) % m != 0:
            t += step
        step *= m

    return t


puzzle_input = aoc_library.read_input('input.txt')

starting_ts = 0
candidate_ts = starting_ts
bus_pos = 0
required_remainders = []
bus_ids = []

for b in puzzle_input[1].split(','):
    if b == 'x':
        bus_pos += 1
        continue
    required_remainders.append(candidate_ts + (1 * bus_pos))
    bus_ids.append(int(b))
    bus_pos += 1

print(required_remainders)
print(bus_ids)
print('Ans: {}'.format(part2_alt(bus_ids, required_remainders)))