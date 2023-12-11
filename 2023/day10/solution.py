from aoc_modules import aoc_library
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


def pad_puzzle(puzzle):
    row_pad = ['.'] * (len(puzzle[0]) + 2)
    for r in puzzle:
        r.insert(0, '.')
        r.append('.')
    puzzle.insert(0, row_pad)
    puzzle.append(row_pad)
    return puzzle


def find_connecting_neighbor(puzzle, row, col, heading):
    current_pipe = puzzle[row][col]
    w_neighbor = puzzle[row][col-1]
    e_neighbor = puzzle[row][col+1]
    s_neighbor = puzzle[row+1][col]
    n_neighbor = puzzle[row-1][col]
    if heading != 'E' and w_neighbor in ('-', 'F', 'L', 'S') and current_pipe in ('-', '7', 'J', 'S'):
        return row, col-1, 'W'
    elif heading != 'S' and n_neighbor in ('|', '7', 'F', 'S') and current_pipe in ('|', 'L', 'J', 'S'):
        return row-1, col, 'N'
    elif heading != 'W' and e_neighbor in ('-', 'J', '7', 'S') and current_pipe in ('-', 'F', 'L', 'S'):
        return row, col+1, 'E'
    elif heading != 'N' and s_neighbor in ('|', 'J', 'L', 'S') and current_pipe in ('|', 'F', '7', 'S'):
        return row+1, col, 'S'
    else:
        print(f'DEADEND: {row=}, {col=}, {heading=}')
        return None


def part1_solve(test=True):
    if test:
        puzzle = aoc_library.read_2d('test_input.txt')
    else:
        puzzle = aoc_library.read_2d('input.txt')
    puzzle = pad_puzzle(puzzle)
    # Find starting point
    position = None
    for r, row in enumerate(puzzle):
        for c, char in enumerate(row):
            if char == 'S':
                position = (r, c)
                # print(r, c)
    steps = 0
    done = False
    row, col = position
    hdg = 'A'
    while not done:
        steps += 1
        # print(f'{row=}, {col=}, {hdg=}')
        row, col, hdg = find_connecting_neighbor(puzzle, row, col, hdg)
        if puzzle[row][col] == 'S':
            done = True
        if steps > len(puzzle) * len(puzzle[0]):
            print('TOO MANY STEPS')
            break
    return steps // 2



def part2_solve(test=True):
    if test:
        puzzle = aoc_library.read_2d('test_input.txt')
    else:
        puzzle = aoc_library.read_2d('input.txt')
    puzzle = pad_puzzle(puzzle)
    # Find starting point
    position = None
    for r, row in enumerate(puzzle):
        for c, char in enumerate(row):
            if char == 'S':
                position = (r, c)
                # print(r, c)
    steps = 0
    row, col = position
    hdg = 'A'
    visited = [(row, col)]
    while True:
        steps += 1
        # print(f'{row=}, {col=}, {hdg=}')
        row, col, hdg = find_connecting_neighbor(puzzle, row, col, hdg)
        if puzzle[row][col] == 'S':
            break
        visited.append((row, col))
    polygon = Polygon(visited)
    print(visited)
    print(polygon)
    ans = 0
    for i, puzzle_row in enumerate(puzzle):
        for j, char in enumerate(puzzle_row):
            if char == '.' and polygon.contains(Point(i, j)):
                ans += 1
    return ans




def main():
    print(f'Part 1 test solution: {part1_solve()}')
    print(f'Part 1 test solution: {part1_solve(test=False)}')

    print(f'Part 2 test solution: {part2_solve()}')
    # print(f'Part 2 test solution: {part2_solve(test=False)}')


if __name__ == "__main__":
    main()
