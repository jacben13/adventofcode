"""TODO(benja): DO NOT SUBMIT without one-line documentation for part1.

TODO(benja): DO NOT SUBMIT without a detailed description of part1.
"""

from collections.abc import Sequence
import re


def read_input(filepath):
  accum = []
  with open(filepath) as f:
    for line in f:
      accum.append(line)
  return accum


def left_num(s):
  numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
  for c in s:
    if c in numbers:
      return c


def right_num(s):
  numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
  for c in s[::-1]:
    if c in numbers:
      return c


def part2_scan(s):
  long_hand = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5',
               'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
  for n in range(1, 10):
    long_hand[str(n)] = str(n)

  long_re = r'(\d|one|two|three|four|five|six|seven|eight|nine).*(\d|one|two|three|four|five|six|seven|eight|nine)'
  single_re = r'(\d|one|two|three|four|five|six|seven|eight|nine)'
  matches = re.search(long_re, s)
  if not matches:
    #print(s)
    single_match = re.search(single_re, s)
    return int(long_hand[single_match.group(1)] * 2)
  return int(long_hand[matches.group(1)] + long_hand[matches.group(2)])


def part1_solve(test=True):
  if test:
    fp = 'test_input.txt'
  else:
    fp = 'input.txt'

  puzzle = read_input(fp)
  answer = 0
  for l in puzzle:
    line_ans = int(left_num(l) + right_num(l))
    #print(line_ans)
    answer += line_ans
  return answer

def part2_solve(test=True):
  if test:
    fp = 'test_input2.txt'
  else:
    fp = 'input.txt'

  puzzle = read_input(fp)
  answer = 0
  for l in puzzle:
    line_ans = part2_scan(l)
    #print(line_ans)
    answer += line_ans
  return answer


def main(argv: Sequence[str]) -> None:

  print(f'Part 1 test answer: {part1_solve()}')
  print(f'Part 1 test answer: {part1_solve(test=False)}')

  print(f'Part 2 test answer: {part2_solve()}')
  print(f'Part 2 test answer: {part2_solve(test=False)}')

if __name__ == "__main__":
  main('hi')
