from aoc_modules import aoc_library
import re


def part1_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('day03/test_input.txt')
    else:
        puzzle = aoc_library.read_input('day03/input.txt')
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    answer = 0
    for line in puzzle:
        result = re.findall(pattern, line)
        for r in result:
            a = int(r[0])
            b = int(r[1])
            answer += a * b
    return answer

    



def part2_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('day03/test_input.txt')
    else:
        puzzle = aoc_library.read_input('day03/input.txt')
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    enable_pattern = r"do\(\)(.*?)don't\(\)"

    answer = 0
    big_puzzle = 'do()'
    for line in puzzle:
        big_puzzle += line
    big_puzzle += "don't()"
    result = re.findall(enable_pattern, big_puzzle)
    for r in result:
        mul_results = re.findall(mul_pattern, r)
        for m in mul_results:
            a = int(m[0])
            b = int(m[1])
            mul = a * b
            answer += mul
    return answer


def main():
    print(f'Part 1 test solution: {part1_solve()}')
    print(f'Part 1 test solution: {part1_solve(test=False)}')

    # print(f'Part 2 test solution: {part2_solve()}')
    print(f'Part 2 test solution: {part2_solve(test=False)}')


if __name__ == "__main__":
    main()
