# Day 3 puzzle, part 1
import os

def add_mountain_slice(line, mountain):
     line = line.rstrip()
     mountain.append(line)

def check_for_tree(slice, x):
    return slice[x] == '#'

def toboggan_move(slice, start_x):
    x = (start_x + 3) % len(slice)
    return x

mountain = []

with open('input.txt') as f:
    for line in f:
        add_mountain_slice(line, mountain)

x = 0
trees_touched = 0
for slice in mountain:
    trees_touched += check_for_tree(slice, x)
    x = toboggan_move(slice, x)

print('Touched {} trees'.format(trees_touched))