from aoc_modules import aoc_library
import copy
from multiprocessing import Pool


class PathError(Exception):
    pass


def find_guard(room_map):
    for y, row in enumerate(room_map):
        for x, c in enumerate(row):
            if c in '><^v':
                return x, y
    print_map(room_map)
    raise(RuntimeError('Guard not found'))


def move_guard(room_map, move_set=set()):
    x, y = find_guard(room_map)
    guard_facing = room_map[y][x]
    move_tuple = (guard_facing, x, y)
    if move_tuple in move_set:
        raise(PathError('Loop Detected'))
    if guard_facing == 'v' and y + 1 == len(room_map):
        room_map[y][x] = 'X'
        return True, room_map, move_set
    elif guard_facing == 'v' and room_map[y+1][x] != '#':
        room_map[y][x] = 'X'
        room_map[y+1][x] = 'v'
        move_set.add(move_tuple)
        return False, room_map, move_set
    elif guard_facing == 'v' and room_map[y+1][x] == '#':
        room_map[y][x] = '<'
        return False, room_map, move_set
    elif guard_facing == '^' and y == 0:
        room_map[y][x] = 'X'
        return True, room_map, move_set
    elif guard_facing == '^' and room_map[y-1][x] != '#':
        room_map[y][x] = 'X'
        room_map[y-1][x] = '^'
        move_set.add(move_tuple)
        return False, room_map, move_set
    elif guard_facing == '^' and room_map[y-1][x] == '#':
        room_map[y][x] = '>'
        return False, room_map, move_set
    elif guard_facing == '<' and x == 0:
        room_map[y][x] = 'X'
        return True, room_map, move_set
    elif guard_facing == '<' and room_map[y][x-1] != '#':
        room_map[y][x] = 'X'
        room_map[y][x-1] = '<'
        move_set.add(move_tuple)
        return False, room_map, move_set
    elif guard_facing == '<' and room_map[y][x-1] == '#':
        room_map[y][x] = '^'
        return False, room_map, move_set
    elif guard_facing == '>' and x + 1 == len(room_map[y]):
        room_map[y][x] = 'X'
        return True, room_map, move_set
    elif guard_facing == '>' and room_map[y][x+1] != '#':
        room_map[y][x] = 'X'
        room_map[y][x+1] = '>'
        move_set.add(move_tuple)
        return False, room_map, move_set
    elif guard_facing == '>' and room_map[y][x+1] == '#':
        room_map[y][x] = 'v'
        return False, room_map, move_set
    else:
        raise(RuntimeError('Could not move guard'))


def count_x(room_map):
    visited = 0
    for row in room_map:
        for c in row:
            if c == 'X':
                visited += 1
    return visited


def print_map(room_map):
    print('*' * 80)
    for r in room_map:
        print(r)


def part1_solve(test=True):
    if test:
        puzzle = aoc_library.read_2d('day06/test_input.txt')
    else:
        puzzle = aoc_library.read_2d('day06/input.txt')
    room_map = puzzle
    # print_map(room_map)
    done = False
    while not done:
        done, new_map, _ = move_guard(room_map)
        # print(f'{done=}')
        # print_map(new_map)
        room_map = new_map
    # print_map(room_map)
    print(f'{count_x(room_map)=}')


def check_obstacle(room_map):
    done = False
    moves = set()
    while not done:
        try:
            done, new_map, moves = move_guard(room_map, moves)
        except PathError:
            return True
        # print(f'{done=}')
        # print_map(new_map)
        room_map = new_map
    return False


def part2_solve(test=True):
    if test:
        puzzle = aoc_library.read_2d('day06/test_input.txt')
    else:
        puzzle = aoc_library.read_2d('day06/input.txt')
    original_room_map = puzzle
    obstacle_options = 0
    # print_map(original_room_map)

    for y, row in enumerate(original_room_map):
        for x, _ in enumerate(row):
            print(f'attempting obstacles at {x}, {y}')
            room_map = copy.deepcopy(original_room_map)
            if room_map[y][x] != '.':
                continue
            else:
                room_map[y][x] = '#'
            obstacle_options += check_obstacle(room_map)
    return obstacle_options


def part2_solve_multiprocess(test=True):
    if test:
        puzzle = aoc_library.read_2d('day06/test_input.txt')
    else:
        puzzle = aoc_library.read_2d('day06/input.txt')
    original_room_map = copy.deepcopy(puzzle)
    x1, y1 = find_guard(original_room_map)
    done = False
    solved_room_map = puzzle
    while not done:
        done, new_map, _ = move_guard(solved_room_map, set())
        if not done:
            solved_room_map = new_map
    solved_room_map[y1][x1] = '^'
    obstacle_options = 0
    # print_map(original_room_map)
    multiprocess_inputs = []
    for y, row in enumerate(solved_room_map):
        for x, _ in enumerate(row):
            room_map = copy.deepcopy(solved_room_map)
            if solved_room_map[y][x] in '^.#':
                continue
            else:
                print(f'attempting obstacles at {x}, {y}')
                room_map[y][x] = '#'
            obstacle_pos = (x, y)
            multiprocess_inputs.append(room_map)
    print(f'About to run {len(multiprocess_inputs)} tasks')
    with Pool() as p:
        results = p.map(check_obstacle, multiprocess_inputs)
    for r in results:
        obstacle_options += r
    return obstacle_options


def main():
    # print(f'Part 1 test solution: {part1_solve()}')
    # print(f'Part 1 test solution: {part1_solve(test=False)}')

    print(f'Part 2 test solution: {part2_solve_multiprocess()}')
    print(f'Part 2 test solution: {part2_solve_multiprocess(test=False)}')


if __name__ == "__main__":
    main()
