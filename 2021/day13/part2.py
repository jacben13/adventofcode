from aoc_modules import aoc_library
from itertools import product
from collections import Counter


puzzle = aoc_library.read_input('input.txt')

sheet = []
folds = []
dots = []
# Figure out dimensions
max_x = 0
max_y = 0
for line in puzzle:
    if line in ['\n', '']:
        continue
    elif 'fold' in line:
        folds.append(line.split()[-1])
    else:
        x, y = line.split(',')
        x = int(x)
        y = int(y)
        max_x = max(x, max_x)
        max_y = max(y, max_y)
        dots.append((x, y))

# Create sheet
for row in range(max_y + 1):
    line = []
    for col in range(max_x + 1):
        line.append(0)
    sheet.append(line)

for dot in dots:
    sheet[dot[1]][dot[0]] = 1

# for r in sheet:
#     print(r)

print(folds)


# Need to consider a fold at a place other than the center
def fold_y(paper, y):
    y_offset = max(y - (len(paper) - y), 0)
    side_a = paper[y_offset:y].copy()
    side_b = paper[:y:-1].copy()
    for i in range(len(side_a)):
        for j in range(len(side_a[0])):
            paper[y_offset + i][j] = side_a[i][j] + side_b[i][j]
    paper = paper[:y]
    return paper


def fold_x(paper, x):
    x_offset = max(x - (len(paper[0]) - x), 0)
    side_a = []
    side_b = []
    for a in paper:
        side_a.append(a[x_offset:x])
        side_b.append(a[:x:-1])
    for i in range(len(paper)):
        for j in range(len(side_a[0])):
            paper[i][x_offset + j] = side_a[i][j] + side_b[i][j]
    new_paper = []
    for i, row in enumerate(paper):
        new_paper.append(row[:x])
    return new_paper


for f in folds:
    dir, pos = f.split('=')
    if dir == 'x':
        sheet = fold_x(sheet, int(pos))
    else:
        sheet = fold_y(sheet, int(pos))

s = ''
for r in sheet:
    for c in r:
        if c:
            s += '█'
        else:
            s += ' '
    s += '\n'

print(s)