from aoc_modules import aoc_library


puzzle = aoc_library.read_input('input.txt')

lines = []
for l in puzzle:
    frag = l.split('->')
    origin = frag[0].replace(' ', '').split(',')
    origin = [int(i) for i in origin]
    terminus = frag[1].replace(' ', '').split(',')
    terminus = [int(i) for i in terminus]
    lines.append([origin, terminus])

line_max = 0
line_sums = []
# Figure out size of board,j fill it with 0s
for y in lines:
    for g in y:
        max_g = max(g)
        line_max = max(max_g, line_max)

line_max += 1
for a in range(line_max):
    line_sums.append([0] * line_max)

# Add line traces for vertical/horizontal lines only
for l in lines:
    if l[0][0] == l[1][0]:
        x = l[0][0]
        for y in range(min(l[0][1], l[1][1]), 1 + max(l[0][1], l[1][1])):
            line_sums[y][x] += 1
    elif l[0][1] == l[1][1]:
        y = l[0][1]
        for x in range(min(l[0][0], l[1][0]), 1 + max(l[0][0], l[1][0])):
            line_sums[y][x] += 1
    else:
        x_step = 1 if l[0][0] < l[1][0] else -1
        y_step = 1 if l[0][1] < l[1][1] else -1
        x = l[0][0]
        y = l[0][1]
        x_done = l[1][0]
        y_done = l[1][1]
        while x != x_done and y != y_done:
            line_sums[y][x] += 1
            x += x_step
            y += y_step
        line_sums[y][x] += 1

for l in line_sums:
    continue
    print(l)

overlap_at_least_2 = 0

for m in line_sums:
    for n in m:
        overlap_at_least_2 += n >= 2

print(f'Overlaps of 2 or more: {overlap_at_least_2}')