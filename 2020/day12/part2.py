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


def rotate_wp(wp_n, wp_e, magnitude):
    while magnitude != 0:
        if magnitude > 0:
            wp_n, wp_e = rotate_wp_90_right(wp_n, wp_e)
            magnitude -= 90
        elif magnitude < 0:
            wp_n, wp_e = rotate_wp_90_left(wp_n, wp_e)
            magnitude += 90
    return wp_n, wp_e


def rotate_wp_90_right(wp_n, wp_e):
    return wp_e * -1, wp_n


def rotate_wp_90_left(wp_n, wp_e):
    return wp_e, wp_n * -1

puzzle_input = aoc_library.read_input('input.txt')

n = 0
e = 0
wp_n = 1
wp_e = 10

for move in puzzle_input:
    decoder = r'([A-Z])(.*)'
    command = re.match(decoder, move).group(1)
    magnitude = int(re.match(decoder, move).group(2))
    print('Ship N: {} E: {} ; WP N: {} WP E: {}'.format(n, e, wp_n, wp_e))
    print('Command: {} Magnitude: {}'.format(command, magnitude))
    if command == 'F':
        n += wp_n * magnitude
        e += wp_e * magnitude

    if command == 'N':
        wp_n += magnitude
    elif command == 'E':
        wp_e += magnitude
    elif command == 'S':
        wp_n -= magnitude
    elif command == 'W':
        wp_e -= magnitude
    elif command == 'L':
        wp_n, wp_e = rotate_wp(wp_n, wp_e, -1 * magnitude)
    elif command == 'R':
        wp_n, wp_e = rotate_wp(wp_n, wp_e, magnitude)


print('Part 2 answer: {}'.format(calc_manhattan_dist(n, e)))