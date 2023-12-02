from aoc_modules import aoc_library
from collections import Counter


puzzle = aoc_library.read_input('input.txt')

heights = []
for l in puzzle:
    h = []
    for n in l:
        h.append(int(n))
    heights.append(h)

sum_of_lows = 0
coords_of_lows = []
for r, row in enumerate(heights):
    for c, col in enumerate(row):
        neighbors = []
        if c > 0:
            neighbors.append(heights[r][c-1])
        if c + 1< len(row):
            neighbors.append(heights[r][c+1])
        if r > 0:
            neighbors.append(heights[r-1][c])
        if r + 1 < len(heights):
            neighbors.append(heights[r+1][c])
        if min(neighbors) > col:
            sum_of_lows += col + 1
            coords_of_lows.append((r, c))

# for each low point
#     check each neighbor for edge or 9
#     add each neighbor to a set with
#     then recursively call their neighbors

def check_and_update_neighbor_list(r, c, set_of_points, heightmap):
    set_of_points.add((r, c))
    if c > 0 and heightmap[r][c - 1] != 9 and (r, c - 1) not in set_of_points:
        check_and_update_neighbor_list(r, c - 1, set_of_points, heightmap)
    if c + 1 < len(row) and heightmap[r][c + 1] != 9 and (r, c + 1) not in set_of_points:
        check_and_update_neighbor_list(r, c + 1, set_of_points, heightmap)
    if r > 0 and heightmap[r - 1][c] != 9 and (r - 1, c) not in set_of_points:
        check_and_update_neighbor_list(r - 1, c, set_of_points, heightmap)
    if r + 1 < len(heights) and heightmap[r + 1][c] != 9 and (r + 1, c) not in set_of_points:
        check_and_update_neighbor_list(r + 1, c, set_of_points, heightmap)
    return set_of_points

ans = []
for r, c in coords_of_lows:
    s = set()
    basin_size = len(check_and_update_neighbor_list(r, c, s, heights))
    print(basin_size)
    ans.append(basin_size)

ans.sort(reverse=True)
print(ans)
print(ans[0] * ans[1] * ans[2])