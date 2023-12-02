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


def find_contiguous_sum(x, list):
    candidate_list = []
    window_start = 0
    window_end = 1
    for y in list:
        while sum_list(candidate_list) <= x:
            candidate_list = list[window_start:window_end]
            if sum_list(candidate_list) == x:
                print('Found candidate list {}'.format(candidate_list))
                return candidate_list
            window_end += 1
        print('Moving window to {}'.format(window_start))
        candidate_list = []
        window_start += 1
        window_end = window_start + 1

def sum_list(l):
    s = 0
    for n in l:
        s += n
    return s


def get_weak_key(short_list):
    return min(short_list) + max(short_list)

key = 0
for n in puzzle_input[window_size:]:
    if not check_number(cursor, window_size, n, puzzle_input):
        print('Found {}'.format(n))
        key = n
        break
    cursor += 1

k = get_weak_key(find_contiguous_sum(key, puzzle_input))
print('Weak key is {}'.format(k))