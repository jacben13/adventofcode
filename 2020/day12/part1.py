from aoc_modules import aoc_library
import re


def calc_manhattan_dist(northing, easting):
    return abs(northing) + abs(easting)


def map_hdg_to_direction(hdg):
    if hdg == 0:
        return 'N'
    elif hdg == 90:
        return 'E'
    elif hdg == 180:
        return 'S'
    elif hdg == 270:
        return 'W'

puzzle_input = aoc_library.read_input('input.txt')

n = 0
e = 0
hdg = 90

for move in puzzle_input:
    decoder = r'([A-Z])(.*)'
    command = re.match(decoder, move).group(1)
    magnitude = int(re.match(decoder, move).group(2))
    # print('Command: {} Magnitude: {}'.format(command, magnitude))
    if command == 'F':
        command = map_hdg_to_direction(hdg)

    if command == 'N':
        n += magnitude
    elif command == 'E':
        e += magnitude
    elif command == 'S':
        n -= magnitude
    elif command == 'W':
        e -= magnitude
    elif command == 'L':
        hdg = (360 + hdg - magnitude) % 360
    elif command == 'R':
        hdg = (360 + hdg + magnitude) % 360

print('Part 1 answer: {}'.format(calc_manhattan_dist(n, e)))