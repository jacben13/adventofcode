from aoc_modules import aoc_library
from itertools import product
from collections import Counter, defaultdict, deque


puzzle = aoc_library.read_input('input.txt')
puzzle = puzzle[0]

print(puzzle)

def hex_to_bin(c):
    decoder = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }
    return decoder[c]


def recurse_subpackets(subpackets, bits=float('inf')):
    ans = 0
    q = deque()
    q.appendleft(('version', bits))
    while q:
        action, bits = q.popleft()
        if not subpackets:
            break
        if action == 'version':
            v = int(subpackets[0:3], 2)
            # print(f'Packet start, version: {v}')
            ans += v
            subpackets = subpackets[3:]
            q.appendleft(('type', bits - 3))
        elif action == 'type':
            a = ('literal', bits - 3) if int(subpackets[0:3], 2) == 4 else ('length_type', bits - 3)
            q.appendleft(a)
            subpackets = subpackets[3:]
        elif action == 'literal':
            some_number = ''
            temp = subpackets
            done = False
            bits_consumed = 0
            while not done:
                if temp[0] == '0':
                    done = True
                some_number += temp[1:5]
                temp = temp[5:]
                bits_consumed += 5
            # print(f'literal found: {int(some_number, 2)}')
            subpackets = subpackets[bits_consumed:]
        elif action == 'length_type':
            if subpackets[0] == '0':
                q.appendleft(('op0', bits - 1))
                subpackets = subpackets[1:]
            elif subpackets[0] == '1':
                q.appendleft(('op1', bits - 1))
                subpackets = subpackets[1:]
        elif action == 'op0':
            # print(f'op0')
            bits_0 = int(subpackets[0:15], 2)
            if bits == float('inf'):
                bits = 0
            q.appendleft(('version', bits_0 + bits))
            subpackets = subpackets[15:]
            ans += recurse_subpackets(subpackets[:bits_0])
            subpackets = subpackets[bits_0:]
        elif action == 'op1':
            # print(f'op1')
            n_packets = int(subpackets[0:11], 2)
            for n in range(n_packets):
                q.appendleft(('version', bits - 11))
            subpackets = subpackets[11:]
        if not q and bits > 0:
            q.appendleft(('version', bits))
    return ans

expanded = ''
for c in puzzle:
    expanded += hex_to_bin(c)

print(expanded)
original_length = len(expanded)

answer = recurse_subpackets(expanded)


print(f'Version sum: {answer}')
