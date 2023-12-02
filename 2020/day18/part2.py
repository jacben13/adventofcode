import aoc_library
import re

def calculate(expression):
    inner_most = r'\([^()]+\)'
    plus_ops = r'\d+ \+ \d+'
    if type(expression) == re.Match:
        expression = expression.group()
        expression = expression[1:-1] if '(' in expression else expression
    acc = 0
    while '(' in expression:
        # calculate the substring that matches via recursion
        # replace the (expression) with calculation
        expression = re.sub(inner_most, calculate, expression)
    while '+' in expression:
        if re.fullmatch(plus_ops, expression):
            break
        expression = re.sub(plus_ops, calculate, expression)
    operator = None
    for c in expression.split(' '):
        if c == '+' or c == '*':
            operator = c
            continue
        else:
            if operator == '+' or not operator:
                acc += int(c)
            else:
                acc *= int(c)
    # print(expression)
    # print(acc)
    return str(acc)



input = aoc_library.read_input('input.txt')

answer_list = []
for e in input:
    answer = calculate(e)
    print('{} = {}'.format(answer, e))
    answer_list.append(int(answer))

print('Sum of all answers: {}'.format(sum(answer_list)))