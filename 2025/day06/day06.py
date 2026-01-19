from aoc_modules import aoc_library


def part1_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('2025\day06\\test_input.txt')
    else:
        puzzle = aoc_library.read_input('2025\\day06\\input.txt')
    new_puzzle = []
    operators = None
    answer = 0
    for line in puzzle:
        line = line.replace('   ', ' ')
        line = line.replace('  ', ' ')
        line = line.strip()
        input = line.split(' ')
        if '*' in input:
            operators = input
            break
        nums = []
        for n in input:
            if n == '':
                continue
            nums.append(int(n))
        new_puzzle.append(nums)
    for col_idx, op in enumerate(operators):
        answer_part = 0
        for row_idx, row in enumerate(new_puzzle):
            if op == '*' and answer_part == 0:
                answer_part = row[col_idx]
            elif op == '*':
                answer_part *= row[col_idx]
            else:
                answer_part += row[col_idx]
        answer += answer_part
    return answer




def part2_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('2025\day06\\test_input.txt')
    else:
        puzzle = aoc_library.read_input('2025\\day06\\input.txt')


def main():
    print(f'Part 1 test solution: {part1_solve()}')
    print(f'Part 1 solution: {part1_solve(test=False)}')

    # print(f'Part 2 test solution: {part2_solve()}')
    # print(f'Part 2 solution: {part2_solve(test=False)}')


if __name__ == "__main__":
    main()
