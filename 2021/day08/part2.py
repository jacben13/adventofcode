from aoc_modules import aoc_library
from collections import Counter


puzzle = aoc_library.read_input('input.txt')

# 2 segments: 1, 4 segments: 4, 3 segments: 7, 7 segments: 8
def decipher(input_list):
    cipher = {}
    while len(cipher) < 10:
        for i in input_list:
            # 2 segments: 1, 4 segments: 4, 3 segments: 7, 7 segments: 8
            if len(i) == 2:
                cipher[1] = i
            elif len(i) == 4:
                cipher[4] = i
            elif len(i) == 3:
                cipher[7] = i
            elif len(i) == 7:
                cipher[8] = i
            # Remaining to decode is 0, 2, 3, 5, 6, 9
            # number:segments needed 0:6, 2:5, 3:5, 5:5, 6:6, 9:6
            # 2, 3, 5 need 5 segments
            elif len(i) == 5:
                # Of 2, 3, 5; only 3 will have both segments of 1
                if 1 in cipher and cipher[1].issubset(i):
                    cipher[3] = i
                # 2 shares 2 elements with 4, 5 shares 3
                elif 4 in cipher and len(cipher[4].intersection(i)) == 2:
                    cipher[2] = i
                elif 4 in cipher and len(cipher[4].intersection(i)) == 3:
                    cipher[5] = i
            # Remaining to decode: 0, 6, 9
            elif len(i) == 6:
                # 5 is not a subset of 0
                if 5 in cipher and not cipher[5].issubset(i):
                    cipher[0] = i
                # 3 is only a subset of 9
                elif 3 in cipher and cipher[3].issubset(i):
                    cipher[9] = i
                elif 9 in cipher and 0 in cipher:
                    cipher[6] = i
    return cipher

def decode_digit(cipher, code):
    s = set(code)
    for k, v in cipher.items():
        if v == s:
            return str(k)
    raise Exception('Cipher did not work')

def decode_number(cipher, coded_num):
    decoded = ''
    for d in coded_num:
        decoded += decode_digit(cipher, d)
    return int(decoded)


outputs = []
inputs = []
for p in puzzle:
    inputs.append(p.split('|')[0].split())
    outputs.append(p.split('|')[1].split())


input_sets = []
for l in inputs:
    set_to_append = []
    for i in l:
        set_to_append.append(set(i))
    input_sets.append(set_to_append)

# test_frag = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab'
# test_sets = []
# for f in test_frag.split():
#     test_sets.append(set(f))
#
# print(test_sets)
# c = decipher(test_sets)
#
# # for i, v in c.items():
# #     print(f'{str(v)}: {i}')
#
# test_decode = 'cdfeb fcadb cdfeb cdbaf'
#
# decoded = ''
# for d in test_decode.split():
#     decoded += decode_digit(c, d)
#     print(f'{d}')
#     print(f'{decoded}')

ans = 0
for i, o in zip(input_sets, outputs):
    c = decipher(i)
    ans += decode_number(c, o)

print(ans)