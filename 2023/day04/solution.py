import re
from aoc_modules import aoc_library


def read_input(filepath):
    accum = []
    with open(filepath) as f:
        for line in f:
            accum.append(line)
    return accum


def calc_winnings(winning_nums, card_nums):
    score = -1
    winning_ints = []
    for n in winning_nums.split():
        winning_ints.append(int(n))

    card_ints = []
    for n in card_nums.split():
        card_ints.append(int(n))
        if int(n) in winning_ints:
            score += 1

    if score >= 0:
        return 2 ** score
    else:
        return 0


def calc_copies(card_index, puzzle_line):
    score = 0
    winning_nums = puzzle_line.split(' | ')[0]
    card_nums = puzzle_line.split(' | ')[1]
    winning_ints = []
    copies = []
    for n in winning_nums.split():
        winning_ints.append(int(n))

    card_ints = []
    for n in card_nums.split():
        card_ints.append(int(n))
        if int(n) in winning_ints:
            score += 1
    if score == 0:
        return None
    end = card_index + score + 1
    for s in range(card_index + 1, end):
        copies.append(s)
    return copies


def calc_clones(puzzle_line):
    score = 0
    winning_nums = puzzle_line.split(' | ')[0]
    card_nums = puzzle_line.split(' | ')[1]
    winning_ints = []
    copies = []
    for n in winning_nums.split():
        winning_ints.append(int(n))

    card_ints = []
    for n in card_nums.split():
        card_ints.append(int(n))
        if int(n) in winning_ints:
            score += 1
    return score


def part1_solve(test=True):
    if test:
        puzzle = read_input('test_input.txt')
    else:
        puzzle = read_input('input.txt')

    card_re = r'Card\s+\d+: (.*) \| (.*)'

    ans = 0
    for l in puzzle:
        matches = re.search(card_re, l)
        if not matches:
            print(l)
        winners = matches.group(1).strip()
        card = matches.group(2).strip()
        # print(f'{winners=}')
        # print(f'{card=}')
        ans += calc_winnings(winners, card)

    return ans


def part2_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('test_input.txt')
    else:
        puzzle = aoc_library.read_input('input.txt')

    puzzle_dict = {}
    card_count = {}
    for i, l in enumerate(puzzle, 1):
        puzzle_dict[i] = l.strip()
        card_count[i] = 1
    clone_scores = {}
    for i, l in enumerate(puzzle, 1):
        clone_scores[i] = calc_clones(l.split(':')[1].strip())

    for card_num, _ in enumerate(puzzle, 1):
        # print(f'about to add {clone_scores[card_num]} cards')
        # Add clone_score * copies of current card to card counts
        if clone_scores[card_num] == 0:
            continue

        for nc in range(card_num + 1, card_num + 1 + clone_scores[card_num]):
            card_count[nc] += card_count[card_num]

    return sum(card_count.values())


def main():
    print(f'Part 1 test answer: {part1_solve()}')
    print(f'Part 1 test answer: {part1_solve(test=False)}')

    print(f'Part 2 test answer: {part2_solve()}')
    print(f'Part 2 test answer: {part2_solve(test=False)}')


if __name__ == "__main__":
    main()
