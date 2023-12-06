from aoc_modules import aoc_library


def parse_puzzle(puzz):
    times = []
    distances = []
    for line in puzz:
        what, nums = line.split(':')
        if what == 'Time':
            for n in nums.split():
                times.append(int(n))
        else:
            for n in nums.split():
                distances.append(int(n))
    return times, distances

def parse_p2_puzzle(puzz):
    times = []
    distances = []
    for line in puzz:
        what, nums = line.split(':')
        if what == 'Time':
            times.append(int(nums.replace(' ', '')))
        else:
            distances.append(int(nums.replace(' ', '')))
    return times, distances

def calc_winning_moves(duration, dist_to_beat):
    winning_moves = 0
    for t in range(1, duration):
        dist = (duration - t) * t
        if dist > dist_to_beat:
            winning_moves += 1
    return winning_moves

def part1_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('test_input.txt')
    else:
        puzzle = aoc_library.read_input('input.txt')
    ans = 1
    times, distances = parse_puzzle(puzzle)
    for time, distance in zip(times, distances):
        ans *= calc_winning_moves(time, distance)
    return ans



def part2_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('test_input.txt')
    else:
        puzzle = aoc_library.read_input('input.txt')
    time, distance = parse_p2_puzzle(puzzle)
    print(f'{time=}')
    print(f'{distance=}')
    return calc_winning_moves(time[0], distance[0])


def main():
    print(f'Part 1 test solution: {part1_solve()}')
    print(f'Part 1 test solution: {part1_solve(test=False)}')

    print(f'Part 2 test solution: {part2_solve()}')
    print(f'Part 2 test solution: {part2_solve(test=False)}')


if __name__ == "__main__":
    main()
