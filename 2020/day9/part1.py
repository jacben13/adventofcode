from aoc_modules import aoc_library

puzzle_input = aoc_library.read_numbers('input.txt')

cursor = 25
window_size = 25

def check_number(c, w, x, list):
    to_check = list[c - w:c]
    to_check_copy = to_check
    for n in to_check:
        for i in to_check_copy:
            if n == i:
                continue
            elif (n + i) == x:
                return True
    return False


for n in puzzle_input[window_size:]:
    if not check_number(cursor, window_size, n, puzzle_input):
        print('Found {}'.format(n))
        break
    cursor += 1