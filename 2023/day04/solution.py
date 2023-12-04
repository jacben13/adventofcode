"""TODO(benja): DO NOT SUBMIT without one-line documentation for solution.

TODO(benja): DO NOT SUBMIT without a detailed description of solution.
"""

import re


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
  score = -1
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
  if score < 0:
    return None
  end = card_index + 2 ** score
  for s in range(card_index+1, end):
    copies.append(s)
  return copies


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
    #print(f'{winners=}')
    #print(f'{card=}')
    ans += calc_winnings(winners, card)

  return ans


def part2_solve(test=True):
  if test:
    puzzle = read_input('test_input.txt')
  else:
    puzzle = read_input('input.txt')

  puzzle_dict = {}
  for i, line in enumerate(puzzle, start=1):
    puzzle_dict[i] = line.split(':')[1].strip()

  ans = 0
  cards_to_score = {}
  for i in range(1, len(puzzle_dict.keys())+1):
    cards_to_score[i] = 1

  scores = {}
  for k, v in puzzle_dict.items():
    winning_nums = v.split(' | ')[0]
    card_nums = v.split(' | ')[1]
    scores[k] = calc_winnings(winning_nums, card_nums)

  for card_num, card in puzzle_dict.items():
    new_cards = calc_copies(card_num, card)
    if not new_cards:
      continue
    for nc in new_cards:
      try:
        cards_to_score[nc] += 1
      except:
        print(nc)
        break

  for k, v in cards_to_score.items():
    ans += scores[k] * v

  print(cards_to_score)
  return ans



def main():
  print(f'Part 1 test answer: {part1_solve()}')
  print(f'Part 1 test answer: {part1_solve(test=False)}')

  print(f'Part 2 test answer: {part2_solve()}')
  #print(f'Part 2 test answer: {part2_solve(test=False)}')



if __name__ == "__main__":
  main()
