import aoc_library
import re


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



def build_sets(lines):
    set_dictionary = {}
    for i, text in enumerate(lines):
        set_dictionary[i] = parse_text_to_set(text)
    all_fields_set = set()
    for s in set_dictionary.values():
        all_fields_set.update(s)
    return set_dictionary, all_fields_set


def check_ticket(ticket, allowed_nums):
    number_list = []
    for n in ticket.split(','):
        number_list.append(int(n))
    invalid_numbers = []
    for n in number_list:
        if n not in allowed_nums:
            invalid_numbers.append(n)
    return invalid_numbers


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

scanning_error_rate = 0
# print(tickets_to_check)
for t in tickets_to_check:
    scanning_error_rate += sum(check_ticket(t, all_possible_numbers))

print('Scanning error rate: {}'.format(scanning_error_rate))