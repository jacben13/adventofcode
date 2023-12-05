from aoc_modules import aoc_library
import re


def next_to_symbol(schemematic, row_num, start, end):
    numbers_period = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.')
    off_row_re = r'([^\d.])'
    l_index = start - 1
    if l_index < 0: l_index = 0
    r_index = end + 1
    # Check same row first
    if start != 0:
        left_neighbor = schemematic[row_num][start-1]
        if left_neighbor not in numbers_period: return True
    if end < len(schemematic[row_num]) - 1:
        right_neighbor = schemematic[row_num][end]
        if right_neighbor not in numbers_period: return True
    # check previous row
    if row_num > 0:
        matches = re.search(off_row_re, schemematic[row_num-1][l_index:r_index])
        if matches: return True
    if row_num + 1 < len(schemematic):
        matches = re.search(off_row_re, schemematic[row_num+1][l_index:r_index])
        if matches: return True
    return False


def gear_ratio_calc(schemematic, row, g_index):
    numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

    first_op = None

    number_re = r'(\d*)'


    number_re = r'(\d+)'
    # Check for left/right neighbors
    left_neighbor = schemematic[row][g_index - 1] in numbers
    if left_neighbor:
        print('left neighbor found!')
        reverse_left_side = schemematic[row][g_index::-1]
        reversed_neighbor = re.search(number_re, reverse_left_side).group(1)
        first_op = int(reversed_neighbor[::-1])

    right_neighbor = schemematic[row][g_index + 1] in numbers
    if right_neighbor:
        neighbor = re.search(number_re, schemematic[row][g_index+1:]).group(1)
        if not first_op: first_op = int(neighbor)
        else: return first_op * int(neighbor)
    # check for up neighbors
    up_matches = re.finditer(number_re, schemematic[row-1])
    for m in up_matches:
        if m.start() - 1 <= g_index <= m.end():
            print(f'up neighbor: {m.group()}')
            if not first_op: first_op = int(m.group())
            else: return int(m.group()) * first_op

    # check for down neighbors
    down_matches = re.finditer(number_re, schemematic[row+1])
    for m in down_matches:
        if m.start() - 1 <= g_index <= m.end():
            print(f'down neighbor: {m.group()}')
            if not first_op: first_op = int(m.group())
            else: return int(m.group()) * first_op

    print(f'only {first_op} found')
    return 0


def p1_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('test_input.txt')
    else:
        puzzle = aoc_library.read_input('input.txt')

    num_re = r'(\d*)'
    ans = 0
    for row, l in enumerate(puzzle):
        number_matches = re.finditer(num_re, l)
        for m in number_matches:
            if m.group() != '':
                # print(f'{m.start()} - {m.end()}, {m.group()}')
                if next_to_symbol(puzzle, row, m.start(), m.end()):
                    ans += int(m.group())
    return ans


def p2_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('test_input.txt')
    else:
        puzzle = aoc_library.read_input('input.txt')

    for line in puzzle:
        line = f'.{line}.'
    line_length = len(puzzle[0])
    puzzle.insert(0, line_length * '.')
    puzzle.append(line_length * '.')

    num_re = r'(\*)'
    ans = 0
    for row, l in enumerate(puzzle):
        number_matches = re.finditer(num_re, l)
        for m in number_matches:
            if m.group() == '*':
              print(f'{row}: {m.start()} - {m.end()}, {m.group()}')
              ans += gear_ratio_calc(puzzle, row, m.start())
              print(ans)
            # if the group is a *, then we need to look for neighboring group or overlap with other lines
    return ans

def main():
    print(f'Part 1 test: {p1_solve()}')
    print(f'Part 1 real: {p1_solve(test=False)}')

    print(f'Part 2 test: {p2_solve()}')
    print(f'Part 2 real: {p2_solve(test=False)}')


if __name__ == '__main__':
    main()