input = [20, 0, 1, 11, 6, 3]


def solve(part):
    if part == 1:
        max_round = 2020 + 1
    else:
        max_round = 30000000 + 1

    previous = {x: (i + 1, i + 1) for i, x in enumerate(input)}

    last = input[-1]
    r = len(input) + 1
    while r < max_round:
        last = previous[last][1] - previous[last][0]
        if last in previous:
            previous[last] = (previous[last][1], r)
        else:
            previous[last] = (r, r)
        r += 1

    print(last)

solve(1)
solve(2)