from aoc_modules import aoc_library
from collections import Counter


class Hand:
    card_decode = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                   '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    def __init__(self, hand, bid, part2=False):
        if part2:
            self.card_decode = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                       '9': 9, 'T': 10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14}
        self.bid = int(bid)
        self.str_hand = hand
        self.numeric_hand = []
        self.hand_counter = Counter()
        self.hand_power = 0
        for h in hand:
            self.numeric_hand.append(self.card_decode[h])
            self.hand_counter[self.card_decode[h]] += 1
        self.most_common = None
        self.second_most = None
        if part2:
            self.jokers = self.hand_counter[1]
        else:
            self.jokers = 0
        if len(self.hand_counter) > 1 and part2:
            del self.hand_counter[1]
        for card, count in self.hand_counter.most_common(2):
            if not self.most_common: self.most_common = count
            elif not self.second_most: self.second_most = count
        if self.most_common + self.jokers == 5 or self.jokers == 5:
            self.hand_power = 7
        elif self.most_common + self.jokers == 4:
            self.hand_power = 6
        elif self.most_common + self.jokers == 3 and self.second_most == 2:
            self.hand_power = 5
        elif self.most_common + self.jokers == 3:
            self.hand_power = 4
        elif self.most_common + self.jokers == 2 and self.second_most == 2:
            self.hand_power = 3
        elif self.most_common + self.jokers == 2 and self.second_most == 2:
            self.hand_power = 2
        elif self.most_common + self.jokers == 2:
            self.hand_power = 1

    def __str__(self):
        return f'{self.str_hand} : {self.hand_power}'

    def __repr__(self):
        return f'{self.str_hand} : {self.hand_power}'


def part1_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('test_input.txt')
    else:
        puzzle = aoc_library.read_input('input.txt')
    ans = 0
    hands = []
    for line in puzzle:
        hand, bid = line.split()
        hands.append(Hand(hand, bid))
    # print(sorted(hands, key=lambda h: (h.hand_power, h.numeric_hand), reverse=True))
    for rank, hand in enumerate(sorted(hands, key=lambda h: (h.hand_power, h.numeric_hand), reverse=False), start=1):
        ans += rank * hand.bid

    return ans

def part2_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('test_input.txt')
    else:
        puzzle = aoc_library.read_input('input.txt')
    ans = 0
    hands = []
    for line in puzzle:
        hand, bid = line.split()
        hands.append(Hand(hand, bid, True))
    print(sorted(hands, key=lambda h: (h.hand_power, h.numeric_hand), reverse=True))
    for rank, hand in enumerate(sorted(hands, key=lambda h: (h.hand_power, h.numeric_hand), reverse=False), start=1):
        ans += rank * hand.bid

    return ans


def main():
    print(f'Part 1 test solution: {part1_solve()}')
    print(f'Part 1 test solution: {part1_solve(test=False)}')

    print(f'Part 2 test solution: {part2_solve()}')
    print(f'Part 2 test solution: {part2_solve(test=False)}')


if __name__ == "__main__":
    main()
