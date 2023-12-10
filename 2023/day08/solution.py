from aoc_modules import aoc_library
import itertools
import math


def build_graph(puzzle_list):
    graph = {}
    for line in puzzle_list:
        parts = line.split(' = ')
        destinations = parts[1].split(', ')
        destinations[0] = destinations[0][1:]
        destinations[1] = destinations[1][:3]
        graph[parts[0]] = destinations
    return graph


def part1_solve(test=True, position='AAA', p2_solve=False):
    if test:
        puzzle = aoc_library.read_input('test_input.txt')
    else:
        puzzle = aoc_library.read_input('input.txt')
    directions = None
    graph_lines = []
    for line in puzzle:
        if not directions:
            directions = itertools.cycle(line)
        if '=' not in line:
            continue
        graph_lines.append(line)
    puzzle_graph = build_graph(graph_lines)
    steps = 0
    print(puzzle_graph)
    for d in directions:
        steps += 1
        # print(f'{steps=}, {position=}, {d=}')
        if d == 'L':
            position = puzzle_graph[position][0]
        elif d == 'R':
            position = puzzle_graph[position][1]
        if position == 'ZZZ' or (p2_solve and position[-1] == 'Z'):
            break
    return steps


def part2_solve(test=True):
    puzzle = aoc_library.read_input('input.txt')
    directions = None
    graph_lines = []
    direction_length = None
    for line in puzzle:
        if not directions:
            directions = itertools.cycle(line)
            direction_length = len(line)
        if '=' not in line:
            continue
        graph_lines.append(line)

    puzzle_graph = build_graph(graph_lines)
    ghosts = []
    for g in puzzle_graph.keys():
        if g[-1] == 'A':
            ghosts.append(g)
    ghost_solutions = {}
    for g in ghosts:
        ghost_solutions[g] = part1_solve(False, position=g, p2_solve=True)
    print(ghost_solutions)
    g_list = list(ghost_solutions.values())
    return math.lcm(*g_list)


def main():
    print(f'Part 1 test solution: {part1_solve()}')
    print(f'Part 1 test solution: {part1_solve(test=False)}')

    # print(f'Part 2 test solution: {part2_solve()}')
    print(f'Part 2 test solution: {part2_solve(test=False)}')


if __name__ == "__main__":
    main()
