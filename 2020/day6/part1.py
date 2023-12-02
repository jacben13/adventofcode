from aoc_modules import aoc_library


def process_group(group):
    char_list = []
    for line in group:
        for char in line:
            if char not in char_list:
                char_list.append(char)
    return len(char_list)
puzzle_input = aoc_library.read_input('input.txt')

group_list = []
line_accumulator = []

for line in puzzle_input:
    if line == '':
        group_list.append(line_accumulator)
        line_accumulator = []
    else:
        line_accumulator.append(line)

group_list.append(line_accumulator)
sum = 0
for group in group_list:
    sum += process_group(group)
print(sum)