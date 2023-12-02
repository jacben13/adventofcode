from aoc_modules import aoc_library
from collections import defaultdict



def count_i(l, i):
    sum = 0
    for n in l:
        sum += int(n[i])
    return sum

def common_i(l, i):
    half = len(l) / 2
    one_count = count_i(l, i)
    if one_count >= half:
        return '1'
    else:
        return '0'

def uncommon_i(l, i):
    half = len(l) / 2
    one_count = count_i(l, i)
    if one_count >= half:
        return '0'
    else:
        return '1'


puzzle = aoc_library.read_input('input.txt')

o2_list = puzzle.copy()
co2_list = puzzle.copy()
o2_string = common_i(o2_list, 0)
co2_string = uncommon_i(co2_list, 0)

for i in range(int(o2_list[0])):
    substring_o2 = o2_string[0:i+1]
    to_del = []
    for s in o2_list:
        if not s.startswith(substring_o2):
            to_del.append(s)
    for d in to_del:
        o2_list.remove(d)
    if len(o2_list) == 1:
        break
    o2_string += common_i(o2_list, i+1)

for i in range(int(o2_list[0])):
    substring_co2 = co2_string[0:i+1]
    to_del = []
    for s in co2_list:
        if not s.startswith(substring_co2):
            to_del.append(s)
    for d in to_del:
        co2_list.remove(d)
    if len(co2_list) == 1:
        break
    co2_string += uncommon_i(co2_list, i + 1)

print(f'O2 reading is {o2_list[0]}')
print(f'CO2 reading is {co2_list[0]}')
ls_check = int(co2_list[0], 2) * int(o2_list[0], 2)
print(f'Life support checksum is {ls_check}')