from aoc_modules import aoc_library


def part1_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('day02/test_input.txt')
    else:
        puzzle = aoc_library.read_input('day02/input.txt')
    safe_reports = 0
    for l in puzzle:
        prev = None
        safe = True
        ascending_count = None
        for n in l.split():
            current = int(n)
            if not prev:
                prev = current
                continue
            if abs(current - prev) > 3:
                print('Too big a gap')
                safe = False
                break
            if current == prev:
                print('Same number')
                safe = False
                break
            if ascending_count == None:
                ascending_count = current > prev
                prev = current
                continue
            else:
                ascending_number = current > prev
                if ascending_count ^ ascending_number:
                    print('counting direction changed')
                    safe = False
                    break
            prev = current

        print(f'{l=} {safe=}')
        if safe:
            safe_reports += 1
    
    return safe_reports


def check_levels(levels):
    prev = None
    safe = True
    ascending_count = None
    unsafe_index = None
    for i, n in enumerate(levels):
        current = int(n)
        if not prev:
            prev = current
            continue
        if abs(current - prev) > 3:
            # print(f'Too big a gap at {i}')
            safe = False
            unsafe_index = i
            break
        if current == prev:
            # print(f'Same number at {i}')
            safe = False
            unsafe_index = i
            break
        if ascending_count == None:
            ascending_count = current > prev
            prev = current
            continue
        else:
            ascending_number = current > prev
            if ascending_count ^ ascending_number:
                print(f'counting direction changed at {i}')
                safe = False
                unsafe_index = i
                break
        prev = current
    
    return safe, unsafe_index


def part2_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('day02/test_input.txt')
    else:
        puzzle = aoc_library.read_input('day02/input.txt')
    
    safe_reports = 0
    for l in puzzle:
        levels = l.split()
        result, unsafe_index = check_levels(levels)
        if result:
            safe_reports += 1
            continue
        else:
            print(levels)
            levels_copy = levels.copy()
            levels.pop(unsafe_index)
            print(f'Attempt 2: {levels}')
            result, _ = check_levels(levels)
            if result:
                safe_reports += 1
                continue
            levels = levels_copy.copy()
            levels.pop(unsafe_index-1)
            print(f'Attempt 3: {levels}')
            result, _ = check_levels(levels)
            if result:
                safe_reports += 1
                continue
            levels = levels_copy.copy()
            levels.pop(0)
            print(f'Attempt 4: {levels}')
            result, _ = check_levels(levels)
            if result:
                safe_reports += 1
    return safe_reports





def main():
    # print(f'Part 1 test solution: {part1_solve()}')
    # print(f'Part 1 test solution: {part1_solve(test=False)}')

    print(f'Part 2 test solution: {part2_solve()}')
    print(f'Part 2 test solution: {part2_solve(test=False)}')


if __name__ == "__main__":
    main()
