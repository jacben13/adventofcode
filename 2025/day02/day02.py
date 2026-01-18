from aoc_modules import aoc_library
import re


def part1_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('2025\day02\\test_input.txt')
    else:
        puzzle = aoc_library.read_input('2025\\day02\\input.txt')
    puzzle = puzzle[0]
    answer = 0
    reg = re.compile(r'^(.+)\1{1}$')
    for id_ranges in puzzle.split(','):
        ids = id_ranges.split('-')
        start = int(ids[0])
        end = int(ids[1])
        for n in range(start, end + 1):
            if re.search(reg, str(n)):
                answer += n
    return answer

    



def part2_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('2025\\day02\\test_input.txt')
    else:
        puzzle = aoc_library.read_input('2025\\day02\\input.txt')
    puzzle = puzzle[0]
    answer = 0
    reg = re.compile(r'^(.+)\1+$')
    for id_ranges in puzzle.split(','):
        ids = id_ranges.split('-')
        start = int(ids[0])
        end = int(ids[1])
        for n in range(start, end + 1):
            if re.search(reg, str(n)):
                answer += n
    return answer


def main():
    print(f'Part 1 test solution: {part1_solve()}')
    print(f'Part 1 test solution: {part1_solve(test=False)}')

    print(f'Part 2 test solution: {part2_solve()}')
    print(f'Part 2 test solution: {part2_solve(test=False)}')


if __name__ == "__main__":
    main()
