from aoc_modules import aoc_library


puzzle = aoc_library.read_input('input.txt')

fish = []
for p in puzzle[0].split(','):
    fish.append(int(p))

days = 80

for d in range(days):
    new_fish = []
    next_day_fish = []
    for f in fish:
        if f > 0:
            next_day_fish.append(f - 1)
        elif f == 0:
            next_day_fish.append(6)
            new_fish.append(8)
    fish = next_day_fish
    fish.extend(new_fish)
    print(f'After Day {d + 1}: {len(fish)}')
    #print(fish)
