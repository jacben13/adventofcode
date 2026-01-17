from aoc_modules import aoc_library


def part1_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('2025\day01\\test_input.txt')
    else:
        puzzle = aoc_library.read_input('2025\\day01\\input.txt')
    pos = 50
    zeroes = 0
    for rotation in puzzle:
        direction = rotation[0]
        steps = int(rotation[1:])
        if direction == 'R':
            pos += steps
        elif direction == 'L':
            pos -= steps
        pos = (pos + 100) % 100
        if pos == 0:
            zeroes += 1
    return zeroes



def part2_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('2025\day01\\test_input.txt')
    else:
        puzzle = aoc_library.read_input('2025\\day01\\input.txt')
    pos = 50
    zeroes = 0
    for rotation in puzzle:
        starting_pos = pos
        direction = rotation[0]
        steps = int(rotation[1:])
        zeroes += steps // 100
        pos += 100
        if direction == 'R':
            pos += steps % 100
        elif direction == 'L':
            pos -= steps % 100
        if starting_pos != 0  and (pos <= 100 or pos >= 200):
            zeroes += 1
        pos = pos % 100
    return zeroes


def main():
    # print(f'Part 1 test solution: {part1_solve()}')
    print(f'Part 1 test solution: {part1_solve(test=False)}')

    print(f'Part 2 test solution: {part2_solve()}')
    print(f'Part 2 test solution: {part2_solve(test=False)}')


if __name__ == "__main__":
    main()
