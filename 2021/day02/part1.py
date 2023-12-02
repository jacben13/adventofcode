from aoc_modules import aoc_library

puzzle_input = aoc_library.read_input('input.txt')


hor_pos = 0
depth = 0

for i in puzzle_input:
    instruction, magnitude = i.split()
    magnitude = int(magnitude)
    if instruction == 'forward':
        hor_pos += magnitude
    elif instruction == 'down':
        depth += magnitude
    elif instruction == 'up':
        depth -= magnitude

pos_check = hor_pos * depth
print(f'Position checksum is {pos_check}')