from aoc_modules import aoc_library
from collections import defaultdict


def parse_lists(puzzle_input):
    list_a, list_b = [], []
    for l in puzzle_input:
        a = l.split()
        list_a.append(int(a[0]))
        list_b.append(int(a[1]))
    list_a.sort()
    list_b.sort()
    return list_a, list_b


def freq_count(num_list):
    fc = defaultdict(lambda: 0)
    for n in num_list:
        fc[n] += 1
    return fc


def part1_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('day01/test_input.txt')
    else:
        puzzle = aoc_library.read_input('day01/input.txt')
    list_a, list_b = parse_lists(puzzle) 
    sum_dist = 0
    for a, b in zip(list_a, list_b):
        sum_dist += abs(a - b)
    return sum_dist



def part2_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('day01/test_input.txt')
    else:
        puzzle = aoc_library.read_input('day01/input.txt')
    list_a, list_b = parse_lists(puzzle) 
    frequencies = freq_count(list_b)
    score = 0
    for n in list_a:
        score += n * frequencies[n]
    return score



def main():
    print(f'Part 1 test solution: {part1_solve()}')
    print(f'Part 1 test solution: {part1_solve(test=False)}')

    print(f'Part 2 test solution: {part2_solve()}')
    print(f'Part 2 test solution: {part2_solve(test=False)}')


if __name__ == "__main__":
    main()
