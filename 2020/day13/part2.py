from aoc_modules import aoc_library
import math

puzzle_input = aoc_library.read_input('test_input.txt')


def check_for_departure(ts, bus_id):
    return (ts % bus_id) == 0


def check_schedule(bus_list, sched):
    for b, t in zip(bus_list, sched):
        if not check_for_departure(t, b):
            return False
    return True


def update_schedule(s):
    new_schedule = []
    for t in s:
        new_schedule.append(t + 1)
    return new_schedule


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
# Determine x where in for the test input we find this equivalency
# Chinese remainder theorem applies here, apparently
# x % bus_id = (x + 1) % bus_id = (x + 2) % bus_id
# or
# x : 0 mod a
# x : 1 mod b
# x : 2 mod c

# Multiply required remainders together
N = 1
for n in required_remainders:
    N *= n

# Determine product of other factors in N without n
n_list = []
for n in required_remainders:
    n_list.append(N / n)

# while not check_schedule(bus_ids, required_schedule):
#     required_schedule = update_schedule(required_schedule)
#     if required_schedule[0] % 1000000 == 0:
#         print(required_schedule[0])
#
# print('Ans: {}'.format(required_schedule[0]))