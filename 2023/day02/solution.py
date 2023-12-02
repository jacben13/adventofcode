from aoc_modules import aoc_library
import re


def make_game_tuple(game_line):
    game_re = r'Game (\d+): (.*)'
    matches = re.search(game_re, game_line)
    id = matches.group(1)
    games = matches.group(2)
    return int(id), games


def check_game(game_string, constraints_dict):
    for g in game_string.split(';'):
        for pull in g.split(','):
            color = pull.strip().split(' ')[1]
            num = int(pull.strip().split(' ')[0])
            if constraints_dict[color] < num:
                return False
    return True


def min_colors(game_string):
    colors = {}
    for g in game_string.split(';'):
        for pull in g.split(','):
            color = pull.strip().split(' ')[1]
            num = int(pull.strip().split(' ')[0])
            if color not in colors.keys() or colors[color] < num:
                colors[color] = num
    power = 1
    for n in colors.values():
        power *= n
    # print(f'{colors} : {power=}')
    return power


def p2_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('test_input.txt')
    else:
        puzzle = aoc_library.read_input('input.txt')

    games_dict = {}
    for g in puzzle:
        id, game = make_game_tuple(g)
        games_dict[id] = game

    power_sum  = 0
    for _, game in games_dict.items():
        power_sum += min_colors(game)
    return power_sum

def p1_solve(test=True):
    p1_constraints = {
        'red' : 12,
        'green' : 13,
        'blue' : 14,
    }

    if test:
        puzzle = aoc_library.read_input('test_input.txt')
    else:
        puzzle = aoc_library.read_input('input.txt')
    games_dict = {}
    for g in puzzle:
        id, game = make_game_tuple(g)
        games_dict[id] = game

    valid_id_sum  = 0
    for id, game in games_dict.items():
       if check_game(game, p1_constraints):
           valid_id_sum += id

    return valid_id_sum


def main():
    print(f'Part 1 test: {p1_solve()}')
    print(f'Part 1 real: {p1_solve(test=False)}')

    print(f'Part 2 test: {p2_solve()}')
    print(f'Part 2 real: {p2_solve(test=False)}')

if __name__ == '__main__':
    main()