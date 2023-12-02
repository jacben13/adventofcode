import math

from aoc_modules import aoc_library
from itertools import product
from collections import Counter, defaultdict, deque
import re
import math


puzzle = aoc_library.read_input('test_input.txt')

beacons = []
scanners = {}
scanner_n = 0
for line in puzzle:
    if line == '':
       scanners[scanner_n] = beacons
       beacons = []
    elif line.startswith('---'):
        scanner_n = re.search(r' (\d*) ', line).group(1)
    else:
        bs = []
        for b in line.split(','):
            bs.append(int(b))
        beacons.append(bs)


def calc_3d_distance(c0, c1):
    x0, y0, z0 = c0
    x1, y1, z1 = c1
    return math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2 + (z1 - z0) ** 2)


# For scanner 0
# Create a set of all distances or maybe vectors between each beacons detected
# Then create a comparison set from each other scanner
# Beacons can be matched if they share at least 11 distances with each other
# Scanners are matched if they share 12 beacons
# Then rectify coordinate system and add beacons to composite scanner

