import re


def parse_puzzle_input(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            if line == '\n': continue
            lines.append(line.strip())
    seeds = []
    puzzle_dict = {}
    for n in lines[0].split(': ')[1].split():
        seeds.append(int(n))
    puzzle_dict['seeds'] = seeds

    seed2soil = []
    soil2fert = []
    fert2water = []
    water2light = []
    light2temp = []
    temp2humid = []
    humid2loc = []
    list_to_append = seed2soil
    for line in lines[2:]:
        if line[0].isnumeric():
            list_to_append.append(line)
        elif line == 'soil-to-fertilizer map:':
            list_to_append = soil2fert
        elif line == 'fertilizer-to-water map:':
            list_to_append = fert2water
        elif line == 'water-to-light map:':
            list_to_append = water2light
        elif line == 'light-to-temperature map:':
            list_to_append = light2temp
        elif line == 'temperature-to-humidity map:':
            list_to_append = temp2humid
        elif line == 'humidity-to-location map:':
            list_to_append = humid2loc

    puzzle_dict = {
        'seeds': seeds,
        'seed2soil': seed2soil,
        'soil2fert': soil2fert,
        'fert2water': fert2water,
        'water2light': water2light,
        'light2temp': light2temp,
        'temp2humid': temp2humid,
        'humid2loc': humid2loc,
    }

    return puzzle_dict


def get_next_step(puzzle_dict, num, step):
    for l in puzzle_dict[step]:
        dest, source, s = l.split()
        dest = int(dest)
        source = int(source)
        source_offset = num - source
        s = int(s)
        if source <= num < source + s:
            return dest + source_offset
    return num


def get_rev_step(puzzle_dict, num, step):
    for l in puzzle_dict[step]:
        source, dest, s = l.split()
        dest = int(dest)
        source = int(source)
        source_offset = num - source
        s = int(s)
        if source <= num < source + s:
            return dest + source_offset
    return num


def part1_solve(test=True):
    if test:
        puzzle = parse_puzzle_input('test_input.txt')
    else:
        puzzle = parse_puzzle_input('input.txt')
    # print(puzzle)

    steps = ['seed2soil', 'soil2fert', 'fert2water', 'water2light', 'light2temp', 'temp2humid', 'humid2loc']
    plant_locations = {}
    for seed in puzzle['seeds']:
        s0 = int(seed)
        s = s0
        for step in steps:
            s = get_next_step(puzzle, s, step)
        plant_locations[s0] = s
    # print(plant_locations)
    return min(plant_locations.values())


def part2_solve(test=True):
    if test:
        puzzle = parse_puzzle_input('test_input.txt')
    else:
        puzzle = parse_puzzle_input('input.txt')
    # print(puzzle)

    steps = ['seed2soil', 'soil2fert', 'fert2water', 'water2light', 'light2temp', 'temp2humid', 'humid2loc']
    plant_locations = {}
    # update list of seeds to be intervals, expressed as tuples
    seed_intervals = []
    done = False

    while not done:
        if len(puzzle['seeds']) == 2:
            done = True
        start = puzzle['seeds'].pop(0)
        end = start + puzzle['seeds'].pop(0) - 1
        seed_intervals.append((start, end))

    for seed in puzzle['seeds']:
    for a in range(hope_start, hope_end):
        # if int(seed) in plant_locations.keys():
        #   continue
        s0 = a
        s = s0
        for step in steps[::-1]:
            s = get_rev_step(puzzle, s, step)
        for r in new_seeds:
            if s in r:
                return s
        if a % 100000 == 0:
            print(a)
        # plant_locations[s0] = s
    # print(plant_locations)
    # return min(plant_locations.values())
    return None


def main():
    print(f'Part 1 test solution: {part1_solve()}')
    print(f'Part 1 test solution: {part1_solve(test=False)}')

    # print(f'Part 2 test solution: {part2_solve()}')
    print(f'Part 2 test solution: {part2_solve(test=False)}')


if __name__ == "__main__":
    main()
