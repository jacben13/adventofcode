from aoc_modules import aoc_library
import re


class Bag:
    def __init__(self, color, contained_bags):
        self.color = color
        self.contained_bags = contained_bags


def parse_contained_bags_string(contained_bags_string):
    contained_bags = {}
    bag_number_regex = r'(\d)'
    bag_color_regex = r'[0-9] (.*) bags?'
    for contained_bag in contained_bags_string.split(','):
        if contained_bag == 'contain no other bags.':
            return None
        contained_bags[
            re.search(bag_color_regex, contained_bag).group(1)] = re.search(
            bag_number_regex, contained_bag).group(1)
    return contained_bags


def parse_rule(rule):
    subject_regex = r'^(.*) bags contain'
    contained_bags_regex = r'contain (.*).$'
    subject = re.search(subject_regex, rule).group(1)
    contained_bags = parse_contained_bags_string(re.search(contained_bags_regex, rule)[0])
    return Bag(subject, contained_bags)


def check_bag_for_target(check_bag, target_bag_color, bag_rules):
    # print('Checking {} bag for {}'.format(check_bag.color, target_bag_color))
    # print(check_bag.color)
    # print(check_bag.contained_bags)
    if not check_bag.contained_bags:
        return False
    elif target_bag_color in check_bag.contained_bags.keys():
        print('{} contains {}'.format(check_bag.color, target_bag_color))
        return True
    else:
        for inner_bag in check_bag.contained_bags.keys():
            result = check_bag_for_target(bag_rules[inner_bag], target_bag_color, bag_rules)
            if result:
                return True
    return False




puzzle_input = aoc_library.read_input('input.txt')

bag_rule_dict = {}
for rule in puzzle_input:
    bag = parse_rule(rule)
    bag_rule_dict[bag.color] = bag

print(bag_rule_dict)

possible_bags = 0
for b in bag_rule_dict.keys():
    possible_bags += check_bag_for_target(bag_rule_dict[b], 'shiny gold', bag_rule_dict)

print('Found {} possible bags'.format(possible_bags))