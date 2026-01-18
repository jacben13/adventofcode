from aoc_modules import aoc_library
import re


def max_and_index(l, end=0):
    if end != 0:
        r = l[:end].copy()
    else:
        r = l.copy()
    max = -1
    max_i = -1
    for i, n in enumerate(r):
        if n > max:
            max = n
            max_i = i
    return max, max_i

def part1_solve(test=True):
    if test:
        puzzle = aoc_library.read_2d('2025\day03\\test_input.txt', convert_to_int=True)
    else:
        puzzle = aoc_library.read_2d('2025\\day03\\input.txt', convert_to_int=True)
    total_jolts = 0
    for bank in puzzle:
        msd = 0
        lsd = 0
        msd, msd_i = max_and_index(bank[:-1])
        lsd, lsd_i = max_and_index(bank[msd_i+1:])
        jolts = f'{msd}{lsd}'
        total_jolts += int(jolts)
    return total_jolts
            

def part2_solve(test=True):
    if test:
        puzzle = aoc_library.read_2d('2025\day03\\test_input.txt', convert_to_int=True)
    else:
        puzzle = aoc_library.read_2d('2025\\day03\\input.txt', convert_to_int=True)
    total_jolts = 0
    for bank in puzzle:
        bank_copy = bank.copy()
        digits = []
        idx = 0
        edx = -11
        # There's a bug here, where we are not updating idx and edx as expected
        while len(digits) < 12:
            new, new_idx = max_and_index(bank_copy, edx)
            bank_copy = bank_copy[new_idx + 1:].copy()
            edx += 1
            digits.append(new)
        jolts = ''
        for d in digits:
            jolts += str(d)
        print(jolts)
        total_jolts += int(jolts)
    return total_jolts


def main():
    print(f'Part 1 test solution: {part1_solve()}')
    print(f'Part 1 solution: {part1_solve(test=False)}')

    print(f'Part 2 test solution: {part2_solve()}')
    print(f'Part 2 solution: {part2_solve(test=False)}')


if __name__ == "__main__":
    main()
