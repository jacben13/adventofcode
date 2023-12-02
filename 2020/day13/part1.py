from aoc_modules import aoc_library
import math

puzzle_input = aoc_library.read_input('input.txt')


def calc_waiting_time(departure, bus_id):
    bus_trips = math.ceil(int(departure) /int(bus_id))
    bus_arrival = int(bus_id) * bus_trips
    print('Bus id: {} arrival_time: {}'.format(int(bus_id), bus_arrival))
    print((bus_trips * int(bus_id)) - int(departure))
    return bus_arrival - int(departure)


departure_ts = int(puzzle_input[0])

best_bus = 0
best_waiting_time = departure_ts
for b in puzzle_input[1].split(','):
    if b == 'x':
        continue
    waiting_time = calc_waiting_time(departure_ts, b)
    if waiting_time < best_waiting_time:
        best_waiting_time = waiting_time
        best_bus = int(b)


print('Best bus: {}\nWaiting time: {}\nAns: {}'.format(best_bus, best_waiting_time, best_bus * best_waiting_time))