from aoc_modules import aoc_library

puzzle_input = aoc_library.read_input('input.txt')

def count_occupied(y, x, seat_map):
    left_bound = 0
    right_bound = 0
    occupied_seats = 0

    # Set left bound
    if x == 0:
        left_bound = 0
    else:
        left_bound = x -1
        occupied_seats += count_occupied_in_slice(seat_map[y][left_bound])

    # Set right bound, when used in slicing, this index is not selected
    if x == len(seat_map[0]) - 1:
        right_bound = x
    else:
        right_bound = x + 1
        occupied_seats += count_occupied_in_slice(seat_map[y][right_bound])

    # Count row above, don't count the row if we're looking at a seat in the top row already
    if y == 0:
        pass
    else:
        occupied_seats += count_occupied_in_slice(seat_map[y-1][left_bound:right_bound + 1])


    # Set bottom bound
    if y == len(seat_map) - 1:
        pass
    else:
        occupied_seats += count_occupied_in_slice(seat_map[y + 1][left_bound:right_bound + 1])

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
    for m in seat_map:
        print(m)

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
            elif seat == '#' and neighbor_count >= 4:
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

print('Part 1 answer: {}'.format(count_occupied_in_map(base_map)))