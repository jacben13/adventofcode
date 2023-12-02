import aoc_library
import re

def sum_register(r):
    return sum(r.values())


def convert_to_bin(x):
    n = int(x)
    return format(n, '036b')


def convert_to_dec(s):
    num = ''
    # print(s)
    for n in s:
        num += n
    # print(int(num, 2))
    return int(num, 2)


def update_register(m, k, v, r):
    number = []
    binary = convert_to_bin(v)
    for x, y in zip(m, binary):
        if x in ('0', '1'):
            number.append(str(x))
        else:
            number.append(str(y))
    # print(convert_to_bin(v))
    # print(m)
    # print(convert_to_bin(convert_to_dec(number)))
    # print('='*20)
    number = convert_to_dec(number)
    r[k] = number

puzzle_input = aoc_library.read_input('input.txt')

mask = ''
register = {}
for line in puzzle_input:
    left = line.split('=')[0].strip()
    if left == 'mask':
        mask = line.split(' = ')[1].strip()
    elif left[0:3] == 'mem':
        value = line.split(' = ')[1].strip()
        key = re.match(r'mem.(\d*).*', left).group(1)
        update_register(mask, key, value, register)

# print(register)
print('Ans: {}'.format(sum_register(register)))