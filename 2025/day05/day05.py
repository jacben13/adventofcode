from aoc_modules import aoc_library


def part1_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('2025\day05\\test_input.txt')
    else:
        puzzle = aoc_library.read_input('2025\\day05\\input.txt')
    fresh_ranges = []
    answer = 0
    for fresh_range in puzzle:
        if '-' not in fresh_range:
            break
        endpoints = fresh_range.split('-')
        
        start = int(endpoints[0])
        end = int(endpoints[1])
        fresh_ranges.append(range(start, end + 1))
    for ingredient in puzzle:
        if ingredient == '' or '-' in ingredient:
            continue
        fresh = False
        ingredient_num = int(ingredient)
        for fresh_range in fresh_ranges:
            if ingredient_num in fresh_range:
                fresh = True
                answer += 1
                break
    return answer



def merge_tuples(t1, t2):
    min_n = min(t1[0], t2[0])
    max_n = max(t1[1], t2[1])
    return (min_n, max_n)

def insert_range(ranges, start, end):
    new_ranges = []
    if len(ranges) == 0:
        return [range(start, end + 1)]
    merged = False
    for r in ranges:
        if start in r and end in r:
            return ranges
        elif start in r:
            r = range(r.start, end + 1)
            merged = True
            new_ranges.append(r)
        elif end in r:
            r = range(start, r.stop)
            merged = True
            new_ranges.append(r)
        else:
            new_ranges.append(r)
    if not merged:
        new_ranges.append(range(start, end + 1))
    return new_ranges
            

def part2_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('2025\day05\\test_input.txt')
    else:
        puzzle = aoc_library.read_input('2025\\day05\\input.txt')
    fresh_ranges = []
    new_puzzle = []
    for fresh_range in puzzle:
        if '-' not in fresh_range:
            break
        endpoints = fresh_range.split('-')
        start = int(endpoints[0])
        end = int(endpoints[1])
        new_puzzle.append((start, end))
    puzzle = sorted(new_puzzle)

    done = False
    while len(puzzle) > 0:
        start, end = puzzle.pop(0)
        fresh_ranges = insert_range(fresh_ranges, start, end)


    answer = 0
    last_range = None
    for r in fresh_ranges:
        answer += r.stop - r.start
        if last_range is None:
            last_range = r
            continue
        elif r.start in last_range or r.stop in last_range:
            print(f'OVERLAP FOUND')
        last_range = r

    return answer


def main():
    print(f'Part 1 test solution: {part1_solve()}')
    print(f'Part 1 solution: {part1_solve(test=False)}')

    print(f'Part 2 test solution: {part2_solve()}')
    print(f'Part 2 solution: {part2_solve(test=False)}')


if __name__ == "__main__":
    main()
