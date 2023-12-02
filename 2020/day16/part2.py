import aoc_library
import re
from collections import defaultdict


def make_set_from_numbers(x, y):
    s = set()
    for n in range(int(x), int(y) + 1):
        s.add(n)
    return s


def parse_text_to_set(text):
    pattern = r'.*: (\d+)-(\d+) or (\d+)-(\d+)'
    data = re.match(pattern, text)
    s = make_set_from_numbers(data.group(1), data.group(2))
    s |= make_set_from_numbers(data.group(3), data.group(4))
    return s


def get_field_name(text):
    return text.split(':')[0]


def build_sets(lines):
    set_dictionary = {}
    for text in lines:
        set_dictionary[get_field_name(text)] = parse_text_to_set(text)
    all_fields_set = set()
    for s in set_dictionary.values():
        all_fields_set.update(s)
    return set_dictionary, all_fields_set


def check_ticket(ticket, allowed_nums):
    number_list = []
    for n in ticket.split(','):
        number_list.append(int(n))
    for n in number_list:
        if n not in allowed_nums:
            return False
    return True


def check_ticket_field(ticket, index, field, rules_dict):
    allowed_set = rules_dict[field]
    num_to_check = int(ticket.split(',')[index])
    # print('Checking {} in {}'.format(num_to_check, allowed_set))
    return num_to_check in allowed_set


def remove_field_from_others(field_dict, field, dont_remove):
    for k, v in field_dict.items():
        if k == dont_remove:
            continue
        elif field in v:
            v.remove(field)
    return field_dict


# puzzle_input = aoc_library.read_input('part2_test_input.txt')
puzzle_input = aoc_library.read_input('input.txt')


line_list = []
for t in puzzle_input:
    if t == '':
        break
    line_list.append(t)
valid_numbers_dict, all_possible_numbers = build_sets(line_list)

tickets_to_check = []
ticket_check_bool = False
for t in puzzle_input:
    if t != 'nearby tickets:' and not ticket_check_bool:
        continue
    elif t == 'nearby tickets:':
        ticket_check_bool = True
        continue

    if ticket_check_bool:
        tickets_to_check.append(t)

# Build new list of valid tickets
valid_ticket_list = []
for t in tickets_to_check:
    if check_ticket(t, all_possible_numbers):
        valid_ticket_list.append(t)

field_map = defaultdict(list)

for i in range(len(valid_ticket_list[0].split(','))):
    ticket_fields = sorted(valid_numbers_dict.keys())
    print('Valid tickets: {} Checking index: {}'.format(len(valid_ticket_list), i))
    if not ticket_fields:
        break
    for f in ticket_fields:
        valid_field = True
        for j, t in enumerate(valid_ticket_list, start=1):
            if not check_ticket_field(t, i, f, valid_numbers_dict):
                valid_field = False
                print('Excluding {} at index {} after checking {} tickets'.format(f, i, j))
                break
        if valid_field:
            print('Mapping {} to index {}'.format(f, i))
            field_map[f].append(i)


print(field_map)

my_ticket = None
ticket_check_bool = False
for t in puzzle_input:
    if t != 'your ticket:' and not ticket_check_bool:
        continue
    elif t == 'your ticket:':
        ticket_check_bool = True
        continue

    if ticket_check_bool:
        my_ticket = t
        break

ans = 1

solved = False
while not solved:
    for k, v in field_map.items():
        if len(v) == 1:
            field_map = remove_field_from_others(field_map, v[0], k)
            print(field_map)
        solved = True
        for v in field_map.values():
            if len(v) > 1:
                solved = False
                break


for k, v in field_map.items():
    field_map[k] = int(v[0])

for k, v in field_map.items():
    if re.match(r'departure', k):
        print('Multiplying {} into answer'.format(k))
        ans *= int(my_ticket.split(',')[int(v)])

print('Ans: {}'.format(ans))