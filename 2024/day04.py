from aoc_modules import aoc_library


def search_xmas(grid, x, y):
    found_xmas = 0
    if grid[y][x] != 'X':
        return 0
    row = grid[y]
    width = len(row)
    height = len(grid)
    # Find forward
    if x <= width - 4 and row[x:x+4] == 'XMAS':
        # print(f'Found fwd xmas at {x=} {y=}')
        found_xmas += 1
    # Find backward
    if x >= 3 and row[x-3:x+1] == 'SAMX':
        # print(f'Found bwd xmas at {x=} {y=}')
        found_xmas += 1
    # Find up
    if y >= 3 and grid[y-1][x] == 'M' and grid[y-2][x] == 'A' and grid[y-3][x] == 'S':
        # print(f'Found up xmas at {x=} {y=}')
        found_xmas += 1
    # Find down
    if y <= height - 4 and grid[y+1][x] == 'M' and grid[y+2][x] == 'A' and grid[y+3][x] == 'S':
        # print(f'Found down xmas at {x=} {y=}')
        found_xmas += 1
    # Find diag right/up
    if y >= 3 and x <= width - 4 and grid[y-1][x+1] == 'M' and grid[y-2][x+2] == 'A' and grid[y-3][x+3] == 'S':
        # print(f'Found right/up xmas at {x=} {y=}')
        found_xmas += 1
    # Find diag right/down
    if y <= height - 4 and x <= width - 4 and grid[y+1][x+1] == 'M' and grid[y+2][x+2] == 'A' and grid[y+3][x+3] == 'S':
        # print(f'Found right/down xmas at {x=} {y=}')
        found_xmas += 1
    # Find diag left/up
    if y >= 3 and x >= 3 and grid[y-1][x-1] == 'M' and grid[y-2][x-2] == 'A' and grid[y-3][x-3] == 'S':
        # print(f'Found left/up xmas at {x=} {y=}')
        found_xmas += 1
    # Find diag left/down
    if y <= height - 4 and x >= 3 and grid[y+1][x-1] == 'M' and grid[y+2][x-2] == 'A' and grid[y+3][x-3] == 'S':
        # print(f'Found left/down xmas at {x=} {y=}')
        found_xmas += 1
    return found_xmas


def search_x_mas(grid, x, y):
    found_xmas = 0
    row = grid[y]
    width = len(row)
    height = len(grid)
    if grid[y][x] != 'A' or x == 0 or y == 0 or x == width - 1 or y == height -1:
        return 0

    pair1 = set()
    pair1.add(grid[y-1][x-1])
    pair1.add(grid[y+1][x+1])
    pair2 = set()
    pair2.add(grid[y-1][x+1])
    pair2.add(grid[y+1][x-1])

    good_set = set()
    good_set.add('M')
    good_set.add('S')

    if pair1 == pair2 and pair1 == good_set:
        found_xmas = 1
    return found_xmas


def part1_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('day04/test_input.txt')
    else:
        puzzle = aoc_library.read_input('day04/input.txt')
    answer = 0
    for y, row in enumerate(puzzle):
        for x, _ in enumerate(row):
            answer += search_xmas(puzzle, x, y)
    return answer


def part2_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('day04/test_input.txt')
    else:
        puzzle = aoc_library.read_input('day04/input.txt')
    answer = 0
    for y, row in enumerate(puzzle):
        for x, _ in enumerate(row):
            answer += search_x_mas(puzzle, x, y)
    return answer


def main():
    print(f'Part 1 test solution: {part1_solve()}')
    print(f'Part 1 test solution: {part1_solve(test=False)}')

    print(f'Part 2 test solution: {part2_solve()}')
    print(f'Part 2 test solution: {part2_solve(test=False)}')


if __name__ == "__main__":
    main()
