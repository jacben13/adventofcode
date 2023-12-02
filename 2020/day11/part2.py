from aoc_modules import aoc_library

puzzle_input = aoc_library.read_input('input.txt')

def create_cardinal_list(y, x, seat_map, vector):
    cardinal_list = []
    if vector == 'U' and y > 0:
        while y > 0:
            y -= 1
            cardinal_list.append(seat_map[y][x])
    elif vector == 'UL' and y > 0 and x > 0:
        while y > 0 and x > 0:
            y -= 1
            x -= 1
            cardinal_list.append(seat_map[y][x])
    elif vector == 'UR' and y > 0 and x < len(seat_map[0]) - 1:
        while y > 0 and x < len(seat_map[0]) - 1:
            y -= 1
            x += 1
            cardinal_list.append(seat_map[y][x])
    elif vector == 'D' and y < len(seat_map) - 1:
        while y < len(seat_map) - 1:
            y += 1
            cardinal_list.append(seat_map[y][x])
    elif vector == 'DR' and y < len(seat_map) - 1 and x < len(seat_map[0]) - 1:
        while y < len(seat_map) - 1 and x < len(seat_map[0]) - 1:
            y += 1
            x += 1
            cardinal_list.append(seat_map[y][x])
    elif vector == 'DL' and y < len(seat_map) - 1 and x > 0:
        while y < len(seat_map) - 1 and x > 0:
            y += 1
            x -= 1
            cardinal_list.append(seat_map[y][x])
    elif vector == 'L' and x > 0:
        while x > 0:
            x -= 1
            cardinal_list.append(seat_map[y][x])
    elif vector == 'R' and x < len(seat_map[0]) - 1:
        while x < len(seat_map[0]) - 1:
            x += 1
            cardinal_list.append(seat_map[y][x])
    return cardinal_list


def check_first_seat(seat_list):
    for s in seat_list:
        if s == 'L':
            return False
        elif s == '#':
            return True
    return False

def count_occupied(y, x, seat_map):
    occupied_seats = 0
    vectors = ['U', 'UR', 'UL', 'D', 'DR', 'DL', 'R', 'L']
    for vector in vectors:
        occupied_seats += check_first_seat(create_cardinal_list(y, x, seat_map, vector))

    return occupied_seats


def count_occupied_in_slice(seat_slice):
    count = 0
    for s in seat_slice:
        if s == '#':
            count += 1
    return count


def count_occupied_in_map(seat_map):
    count = 0
    for s in seat_map:
        count += count_occupied_in_slice(s)
    return count


def evolve_map(seat_map):
    new_map = []
    # for m in seat_map:
    #     print(m)

    for i in range(len(seat_map)):
        seat_row = []
        for j in range(len(seat_map[0])):
            seat = seat_map[i][j]
            if seat == '.':
                seat_row.append('.')
                continue
            neighbor_count = count_occupied(i, j, seat_map)
            if seat == 'L' and neighbor_count == 0:
                seat_row.append('#')
            elif seat == '#' and neighbor_count >= 5:
                seat_row.append('L')
            else:
                seat_row.append(seat)
        new_map.append(seat_row)

    return new_map


occupied_seat_map = []
for i in range(len(puzzle_input)):
    seat_row = []
    for j in range(len(puzzle_input[0])):
        seat_row.append(count_occupied(i, j, puzzle_input))
    occupied_seat_map.append(seat_row)

for m in occupied_seat_map:
    print(m)

base_map = puzzle_input
new_map = evolve_map(puzzle_input)

iterations = 1

while base_map != new_map:
    base_map = new_map
    new_map = evolve_map(base_map)
    iterations += 1
    print(iterations)

print('Part 2 answer: {}'.format(count_occupied_in_map(base_map)))