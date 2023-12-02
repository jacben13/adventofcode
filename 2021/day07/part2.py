from aoc_modules import aoc_library
from collections import Counter


puzzle = aoc_library.read_input('input.txt')

def fuel_exp(a, b):
    # Return fuel cost to move from position a to position b
    d = abs(b - a)
    return d * (d + 1) // 2



crabs = []
for p in puzzle[0].split(','):
    crabs.append(int(p))

crab_positions = Counter(crabs)

max_pos = max(crabs)

least_fuel = max_pos * len(crabs) ** 2
best_position = None
for p in range(max_pos):
    fuel_computation = crab_positions.copy()
    for k, v in fuel_computation.items():
        fuel_computation[k] = fuel_exp(k, p) * v
    fuel_needed = sum(fuel_computation.values())
    if fuel_needed < least_fuel:
        least_fuel = fuel_needed
        best_position = p

print(f'Best position: {best_position}')
print(f'Fuel needed: {least_fuel}')