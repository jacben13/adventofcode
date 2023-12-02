import aoc_library


puzzle_input = aoc_library.read_input('input.txt')
puzzle_input = puzzle_input[0].split(',')
# puzzle_input = [3, 1, 2]

number_set = set()
game_dict = {}
last_turn = None
for i, l in enumerate(puzzle_input, start=1):
    last_turn = int(puzzle_input[i - 1])
    number_set.add(last_turn)
    game_dict[last_turn] = i
    print('Turn {}: {}'.format(i, last_turn))
number_set.remove(last_turn)

goal_turn = 30000000
for i in range(len(puzzle_input) + 1, goal_turn + 1):
    if last_turn not in number_set:
        game_dict[last_turn] = i - 1
        number_set.add(last_turn)
        last_turn = 0
    else:
        ans = (i - 1) - game_dict[last_turn]
        game_dict[last_turn] = i - 1
        last_turn = ans



print('Turn {}: {}'.format(goal_turn, last_turn))