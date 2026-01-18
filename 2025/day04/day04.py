from aoc_modules import aoc_library
import itertools
import copy


def count_neighbors(grid, row, column):
    neighbor_count = 0
    neighbors = [-1, 0, 1]
    for neighbor_row, neighbor_column in itertools.product(neighbors, neighbors):
        if row + neighbor_row < 0 or column + neighbor_column < 0:
            continue
        if neighbor_row == 0 and neighbor_column == 0:
            continue
        try:
            if grid[row + neighbor_row][column + neighbor_column] == 1:
                neighbor_count += 1
        except IndexError:
            continue
    return neighbor_count


def part1_solve(test=True):
    if test:
        puzzle = aoc_library.read_2d('2025\day04\\test_input.txt')
    else:
        puzzle = aoc_library.read_2d('2025\\day04\\input.txt')
    new = []
    for line in puzzle:
        new_line = []
        for c in line:
            if c == '@':
                new_line.append(1)
            else:
                new_line.append(0)
        new.append(new_line)
    puzzle = new
    answer = 0
    good_rolls = copy.deepcopy(puzzle)
    for row_idx, row in enumerate(puzzle):
        for col_idx, col in enumerate(row):
            if col == 1:
                neighbors = count_neighbors(puzzle, row_idx, col_idx)
                if neighbors < 4:
                    answer += 1
                    good_rolls[row_idx][col_idx] = 'X'
    return answer



def part2_solve(test=True):
    if test:
        puzzle = aoc_library.read_2d('2025\day04\\test_input.txt')
    else:
        puzzle = aoc_library.read_2d('2025\\day04\\input.txt')
    new = []
    for line in puzzle:
        new_line = []
        for c in line:
            if c == '@':
                new_line.append(1)
            else:
                new_line.append(0)
        new.append(new_line)
    puzzle = new
    accesible_rolls = 1
    answer = 0
    while accesible_rolls > 0:
        accesible_rolls = 0
        good_rolls = copy.deepcopy(puzzle)
        for row_idx, row in enumerate(puzzle):
            for col_idx, col in enumerate(row):
                if col == 1:
                    neighbors = count_neighbors(puzzle, row_idx, col_idx)
                    if neighbors < 4:
                        answer += 1
                        accesible_rolls += 1
                        good_rolls[row_idx][col_idx] = 'X'
        puzzle = good_rolls
    return answer


def main():
    print(f'Part 1 test solution: {part1_solve()}')
    print(f'Part 1 solution: {part1_solve(test=False)}')

    print(f'Part 2 test solution: {part2_solve()}')
    print(f'Part 2 solution: {part2_solve(test=False)}')


if __name__ == "__main__":
    main()
