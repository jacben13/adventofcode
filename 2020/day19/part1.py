import aoc_library
import re


def parse_rules(rule, rules_d):
    rule_n = rule.split(':')[0].strip()
    rules_d[rule_n] = rule.split(':')[1].strip().replace('"', '')


def decompose_rules(rules_d, key):
    # a_rule_n = list(rules_d.keys())[list(rules_d.values()).index('a')]
    # b_rule_n = list(rules_d.keys())[list(rules_d.values()).index('b')]
    # a_regex = r'\b{}\b'.format(a_rule_n)
    # b_regex = r'\b{}\b'.format(b_rule_n)
    



input = aoc_library.read_input('test_input.txt')

rules = []
msgs = []
read_msg = False

for l in input:
    if l == '':
        read_msg = True
        continue
    if read_msg:
        msgs.append(l)
    else:
        rules.append(l)

rule_dict = {}
for r in rules:
    parse_rules(r, rule_dict)

print(rule_dict)
print(decompose_rules(rule_dict))