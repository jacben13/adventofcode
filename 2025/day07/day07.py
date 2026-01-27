from aoc_modules import aoc_library
import collections


def part1_solve(test=True):
    if test:
        puzzle = aoc_library.read_2d('2025\\day07\\test_input.txt')
    else:
        puzzle = aoc_library.read_2d('2025\\day07\\input.txt')
    answer = 0
    prev_beams = set()
    for line in puzzle:
        next_beams = set()
        splits = set()
        for i, c in enumerate(line):
            if c == 'S' or (c == '.' and i in prev_beams):
                next_beams.add(i)
            # Split
            elif c == '^' and i in prev_beams:
                next_beams.add(i - 1)
                next_beams.add(i + 1)
                if i - 1 not in splits or i + 1 not in splits:
                    answer += 1
                    splits.add(i - 1)
                    splits.add(i + 1)
        prev_beams = next_beams
    
    return answer


def propagate_tachyons(tachyons, splitters):
    new_tachyons = collections.defaultdict(int)
    for tachyon_pos, tachyon_count in tachyons.items():
        if tachyon_pos in splitters:
            new_tachyons[tachyon_pos - 1] += tachyon_count
            new_tachyons[tachyon_pos + 1] += tachyon_count
        else:
            new_tachyons[tachyon_pos] += tachyon_count

    return new_tachyons

def part2_solve(test=True):
    if test:
        puzzle = aoc_library.read_2d('2025\\day07\\test_input.txt')
    else:
        puzzle = aoc_library.read_2d('2025\\day07\\input.txt')
    tachyons = collections.defaultdict(int)
    start_point = None
    for i, c in enumerate(puzzle[0]):
        if c == 'S':
            start_point = i
            break
    tachyons[start_point] += 1
    splitter_rows = []
    for line in puzzle[1:]:
        splitters = []
        if '^' not in line:
            continue
        for i, c in enumerate(line):
            if c == '^':
                splitters.append(i)
        splitter_rows.append(splitters)
    for row in splitter_rows:
        tachyons = propagate_tachyons(tachyons, row)

    
    return sum(tachyons.values())


def main():
    print(f'Part 1 test solution: {part1_solve()}')
    print(f'Part 1 solution: {part1_solve(test=False)}')

    print(f'Part 2 test solution: {part2_solve()}')
    print(f'Part 2 solution: {part2_solve(test=False)}')


if __name__ == "__main__":
    main()
