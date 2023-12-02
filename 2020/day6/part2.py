from aoc_modules import aoc_library


def process_group(group):
    group_size = len(group)
    if group_size == 1:
        return len(group[0])

    char_dict = {}

    for line in group:
        for char in line:
            if char not in char_dict.keys():
                char_dict[char] = 1
            else:
                char_dict[char] += 1

    everyone_yes = 0
    for k in char_dict.keys():
        everyone_yes += char_dict[k] == group_size
    return everyone_yes


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