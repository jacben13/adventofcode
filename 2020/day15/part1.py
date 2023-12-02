import aoc_library


def game_logic(game_list):
    n = game_list[-1]
    if n not in game_list[:-1]:
        # print('New number: {}'.format(n))
        game_list.append(0)
    else:
        for i, x in enumerate(reversed(game_list[:-1]), start=1):
            if x == n:
                delta_turns = i
                # print('Previously saw {} delta turns {}'.format(x, delta_turns))
                game_list.append(delta_turns)
                break


puzzle_input = aoc_library.read_input('input.txt')
puzzle_input = puzzle_input[0].split(',')

number_list = []
for i in range(1, 2021):
    if i - 1 < len(puzzle_input):
        turn_n = puzzle_input[i - 1]
        number_list.append(int(turn_n))
        print('Turn {}: {}'.format(i, turn_n))
        continue
    game_logic(number_list)
    turn_n = number_list[-1]

print('Turn 2020: {}'.format(turn_n))