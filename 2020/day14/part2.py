import aoc_library
import itertools
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


def count_xs(address):
    sum = 0
    for c in address:
        sum += c == 'X'
    return sum


def map_addresses(address):
    prems = ['0', '1']
    prems = itertools.product(prems, repeat=count_xs(address))
    new_addresses = []
    for p in prems:
        new_address = []
        i = 0
        for c in address:
            if c == 'X':
                new_address.append(p[i])
                i += 1
            else:
                new_address.append(c)
        new_addresses.append(new_address)
    print('Preparing to update {} addresses'.format(len(new_addresses)))
    return new_addresses


def update_registers(m, k, v, r):
    address = []
    binary = convert_to_bin(k)
    for x, y in zip(m, binary):
        if x == '0':
            address.append(str(y))
        elif x == '1':
            address.append('1')
        else:
            address.append('X')
    # print(binary)
    # print(m)
    # print(address)
    # print('='*35)
    for a in map_addresses(address):
        r[str(convert_to_dec(a))] = int(v)

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
        update_registers(mask, key, value, register)

# print(register)
print('Ans: {}'.format(sum_register(register)))