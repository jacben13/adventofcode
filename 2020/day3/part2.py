# Day 3 puzzle, part 2
import os

def add_mountain_slice(line, mountain):
     line = line.rstrip()
     mountain.append(line)

def check_for_tree(slice, x):
    return slice[x] == '#'

def toboggan_move(slice, start_x, move):
    x = (start_x + move) % len(slice)
    return x

mountain = []

with open('input.txt') as f:
    for line in f:
        add_mountain_slice(line, mountain)

x1 = 0
x3 = 0
x5 = 0
x7 = 0
y = 0
trees_touched_1 = 0
trees_touched_3 = 0
trees_touched_5 = 0
trees_touched_7 = 0
trees_touched_1_2 = 0
for slice in mountain:
    trees_touched_1 += check_for_tree(slice, x1)
    if (y % 2) == 1:
        trees_touched_1_2 += check_for_tree(slice, x1)
    trees_touched_3 += check_for_tree(slice, x3)
    trees_touched_5 += check_for_tree(slice, x5)
    trees_touched_7 += check_for_tree(slice, x7)
    x1 = toboggan_move(slice, x1, 1)
    x3 = toboggan_move(slice, x3, 3)
    x5 = toboggan_move(slice, x5, 5)
    x7 = toboggan_move(slice, x7, 7)
    y += 1

trees_touched = trees_touched_1 * trees_touched_3 * trees_touched_5 * trees_touched_7 * trees_touched_1_2
print('Right 1, down 1: {} trees'.format(trees_touched_1))
print('Right 3, down 1: {} trees'.format(trees_touched_3))
print('Right 5, down 1: {} trees'.format(trees_touched_5))
print('Right 7, down 1: {} trees'.format(trees_touched_7))
print('Right 1, down 2: {} trees'.format(trees_touched_1_2))
print('Touched {} trees'.format(trees_touched))