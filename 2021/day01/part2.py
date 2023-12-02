from aoc_modules import aoc_library


i = aoc_library.read_numbers('input.txt')

increases = 0
previous = sum(i[0:3])

while len(i) >= 3:
    if len(i) == 3:
        window_sum = sum(i)
    else:
        window_sum = sum(i[0:3])
    if window_sum > previous:
        increases += 1
    previous = window_sum
    i.pop(0)

print(f'There were {increases} increases')
