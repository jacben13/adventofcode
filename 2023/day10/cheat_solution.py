from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    arr = [val.strip() for val in lines]

    # Find the starting (row, col)
    start_row, start_col = -1, -1
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if arr[row][col] == "S":
                start_row = row
                start_col = col
                break

    assert start_row != -1
    assert start_col != -1

    frontier = [(start_row, start_col, 0)]
    visited = set()
    points = []
    best_distance = 0
    while len(frontier) > 0:
        (curr_row, curr_col, curr_dist) = frontier[0]

        frontier.pop(0)

        # Check if row and col are valid
        if curr_row < 0 or curr_row > len(arr) - 1 or curr_col < 0 or curr_col > len(arr[0]) - 1:
            continue

        # Check if we've already been here
        if (curr_row, curr_col) in visited:
            continue

        # Add to visited
        visited.add((curr_row, curr_col))
        points.append((curr_row, curr_col))

        # Look at current distance
        best_distance = max(best_distance, curr_dist)

        # Expand
        if arr[curr_row][curr_col] == "|":
            frontier.append((curr_row - 1, curr_col, curr_dist + 1))
            frontier.append((curr_row + 1, curr_col, curr_dist + 1))
        elif arr[curr_row][curr_col] == "-":
            frontier.append((curr_row, curr_col - 1, curr_dist + 1))
            frontier.append((curr_row, curr_col + 1, curr_dist + 1))
        elif arr[curr_row][curr_col] == "L":
            frontier.append((curr_row - 1, curr_col, curr_dist + 1))
            frontier.append((curr_row, curr_col + 1, curr_dist + 1))
        elif arr[curr_row][curr_col] == "J":
            frontier.append((curr_row - 1, curr_col, curr_dist + 1))
            frontier.append((curr_row, curr_col - 1, curr_dist + 1))
        elif arr[curr_row][curr_col] == "7":
            frontier.append((curr_row, curr_col - 1, curr_dist + 1))
            frontier.append((curr_row + 1, curr_col, curr_dist + 1))
        elif arr[curr_row][curr_col] == "F":
            frontier.append((curr_row, curr_col + 1, curr_dist + 1))
            frontier.append((curr_row + 1, curr_col, curr_dist + 1))
        elif arr[curr_row][curr_col] == "S":
            # Check which directions to go
            if arr[curr_row - 1][curr_col] == "|" or arr[curr_row - 1][curr_col] == "7" or arr[curr_row - 1][curr_col] == "F":
                frontier.append((curr_row - 1, curr_col, curr_dist + 1))
                continue
            if arr[curr_row + 1][curr_col] == "|" or arr[curr_row + 1][curr_col] == "L" or arr[curr_row + 1][curr_col] == "J":
                frontier.append((curr_row + 1, curr_col, curr_dist + 1))
                continue
            if arr[curr_row][curr_col - 1] == "-" or arr[curr_row][curr_col - 1] == "L" or arr[curr_row][curr_col - 1] == "F":
                frontier.append((curr_row, curr_col - 1, curr_dist + 1))
                continue
            if arr[curr_row][curr_col + 1] == "-" or arr[curr_row][curr_col + 1] == "J" or arr[curr_row][curr_col + 1] == "7":
                frontier.append((curr_row, curr_col + 1, curr_dist + 1))
                continue

    print("Part 1:", (best_distance + 1) // 2)

    # Make a polygon out of the data in the visited set
    polygon = Polygon(points)
    # print(polygon)

    ans = 0
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if (row, col) in visited:
                continue

            point = Point(row, col)

            if polygon.contains(point):
                ans += 1

    print("Part 2:", ans)



if __name__ == "__main__":
    main()