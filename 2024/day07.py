from aoc_modules import aoc_library
import itertools


def parse_inputs(line):
    answer, operants = line.split(':')
    answer = int(answer)
    ops = []
    for o in operants.split(' '):
        if o == '':
            continue
        ops.append(int(o))
    return answer, ops


def check_operation(answer, operants, operands):
    temp_answer = None
    operants_stack = list(operants)
    operands_stack = list(operands)
    temp_answer = operants_stack.pop(0)
    for o in operands:
        a = operants_stack.pop(0)
        if o == '+':
            temp_answer += a
        elif o == '|':
            s = str(temp_answer) + str(a)
            temp_answer = int(s)
        else:
            temp_answer *= a
    return temp_answer == answer




def part1_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('day07/test_input.txt')
    else:
        puzzle = aoc_library.read_input('day07/input.txt')
    solution = 0
    for line in puzzle:
        answer, operants = parse_inputs(line)
        operands = itertools.product('+*', repeat=(len(operants)-1))
        for ops in operands:
            if check_operation(answer, operants, ops):
                solution += answer
                break
    return solution



def part2_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('day07/test_input.txt')
    else:
        puzzle = aoc_library.read_input('day07/input.txt')
    solution = 0
    for line in puzzle:
        answer, operants = parse_inputs(line)
        operands = itertools.product('+*|', repeat=(len(operants)-1))
        for ops in operands:
            if check_operation(answer, operants, ops):
                solution += answer
                break
    return solution


def main():
    print(f'Part 1 test solution: {part1_solve()}')
    print(f'Part 1 test solution: {part1_solve(test=False)}')

    print(f'Part 2 test solution: {part2_solve()}')
    print(f'Part 2 test solution: {part2_solve(test=False)}')


if __name__ == "__main__":
    main()
