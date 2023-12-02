from aoc_modules import aoc_library

i = aoc_library.read_numbers('input.txt')

increases = 0
previous = i[0]

for x in i:
    if x > previous:
        increases += 1
    previous = x

print(f'There were {increases} increases')
