from aoc_modules import aoc_library
from collections import defaultdict

puzzle = aoc_library.read_input('input.txt')

def return0():
    return 0

occurence_dict = defaultdict(return0)
at_least_this_common = len(puzzle) // 2

for num in puzzle:
    for i, s in enumerate(num):
        occurence_dict[i] += int(s)

gamma_string = ''
epsilon_string = ''

for item, val in occurence_dict.items():
    if int(val) > at_least_this_common:
        gamma_string += '1'
        epsilon_string += '0'
    else:
        gamma_string += '0'
        epsilon_string += '1'

gamma_dec = int(gamma_string, 2)
epsilon_dec = int(epsilon_string, 2)

print(f'{gamma_string}, is {gamma_dec}')
print(f'{epsilon_string}, is {epsilon_dec}')

print(epsilon_dec * gamma_dec)
