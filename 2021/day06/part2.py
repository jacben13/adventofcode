from aoc_modules import aoc_library


puzzle = aoc_library.read_input('input.txt')

fish = {}
for p in puzzle[0].split(','):
    if int(p) in fish.keys():
        fish[int(p)] += 1
    else:
        fish[int(p)] = 1

print(fish)

days = 256

for d in range(days):
    next_day_fish = {}
    new_fish = 0
    for k, v in fish.items():
        if k == 0:
            if 6 in next_day_fish.keys():
                next_day_fish[6] += v
            else:
                next_day_fish[6] = v
            new_fish += v
        else:
            if k - 1 in next_day_fish.keys():
                next_day_fish[k - 1] += v
            else:
                next_day_fish[k - 1] = v
    fish = next_day_fish
    fish[8] = new_fish
    print(f'After Day {d + 1}: {sum(fish.values())}')
    # print(fish)
