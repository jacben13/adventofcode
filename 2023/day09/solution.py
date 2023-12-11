from aoc_modules import aoc_library


def create_regression(series):
    new_series = []
    all_zero = True
    for i, n in enumerate(series[1:], 1):
        new_n = n - series[i - 1]
        new_series.append(new_n)
        if new_n != 0: all_zero = False
    if all_zero:
        return new_series
    else:
        next_series = create_regression(new_series)
        if type(next_series[0]) == list:
            return [new_series, *next_series]
        else:
            return [new_series, next_series]


def make_prediction(regression_series, x):
    target_length = len(regression_series[0]) + 1
    regression_tuples = []
    regression_series[-1] = [0] * target_length
    for n, l in enumerate(regression_series):
       regression_tuples.append((n, l))
    for i, line in regression_tuples[-2::-1]:
        while len(line) < target_length:
            current_length = len(line)
            line.append(line[-1] + regression_tuples[i+1][1][current_length-1])
    return x + regression_tuples[0][1][-1]


def part1_solve(test=True, reverse=False):
    if test:
        puzzle = aoc_library.read_input('test_input.txt')
    else:
        puzzle = aoc_library.read_input('input.txt')
    new_puzzle = []
    for p in puzzle:
        new_p = []
        for n in p.split():
            new_p.append(int(n))
        if reverse:
            new_puzzle.append(new_p[::-1])
        else:
            new_puzzle.append(new_p)
    puzzle = new_puzzle
    regression_lines = []
    ans = 0
    for l in puzzle:
        print(l)
        regression_lines.append(create_regression(l))
        prediction = make_prediction(regression_lines[-1], l[-1])
        print(f'{prediction=}')
        ans += prediction
    return ans


def part2_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('test_input.txt')
    else:
        puzzle = aoc_library.read_input('input.txt')
    return part1_solve(test=test, reverse=True)


def main():
    print(f'Part 1 test solution: {part1_solve()}')
    print(f'Part 1 test solution: {part1_solve(test=False)}')

    print(f'Part 2 test solution: {part2_solve()}')
    print(f'Part 2 test solution: {part2_solve(test=False)}')


if __name__ == "__main__":
    main()
