from aoc_modules import aoc_library
from collections import defaultdict

puzzle = aoc_library.read_input('input.txt')

class Board:
    def __init__(self, board_string):
        self.board = []
        board_lines = board_string.splitlines()
        for l in board_lines:
            self.board.append(l.split())

    def __str__(self):
        s = ''
        for l in self.board:
            s += f'{l}\n'
        s += '\n'
        return s

    def call_number(self, num):
        for l in self.board:
            for i, n in enumerate(l):
                if n == num:
                    l[i] = 'X'

    def check_for_bingo(self):
        # Check rows
        for l in self.board:
            xs = 0
            for n in l:
                if n == 'X':
                    xs += 1
            if xs == 5:
                return True
        # Check columns
        for i in range(len(self.board)):
            column_list = []
            column_bingo = True
            for j in range(len(self.board[0])):
                if self.board[i][j] != 'X':
                    column_bingo = False
                    break
            if column_bingo:
                return True
        return False

    def score_board(self, winning_num):
        sum = 0
        for r in self.board:
            for n in r:
                if n == 'X':
                    continue
                sum += int(n)
        return sum * int(winning_num)

build_a_board = ''
board_list = []
board_line_count = 0
for l in puzzle:
    if ',' in l:
        print('This is the draw line')
        print(l)
        continue
    elif l == '':
        board_line_count = 0
        build_a_board = ''
        continue
    build_a_board += l
    build_a_board += '\n'
    board_line_count += 1
    if board_line_count == 5:
        board_list.append(Board(build_a_board))
        board_line_count = 0
        build_a_board = ''

call_list = puzzle[0].split(',')
bingo = False
for i, c in enumerate(call_list):
    if bingo:
        break
    for j, b in enumerate(board_list):
        b.call_number(c)
        if b.check_for_bingo():
            print(f'Board #{j+1} is the winner')
            print(f'Winning number: {c}')
            print(f'Score: {b.score_board(c)}')
            bingo = True
            break

# for b in board_list:
#     print(b)
#     print('-' * 4