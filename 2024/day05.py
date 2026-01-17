from aoc_modules import aoc_library


def parse_input(input):
    rules = []
    page_list = []
    for l in input:
        if len(l) == 0:
            continue
        elif '|' not in l:
            single_order = []
            for n in l.split(','):
                single_order.append(int(n))
            page_list.append(single_order)
        else:
            rule = l.split('|')
            a, b = rule
            rules.append(tuple([int(a), int(b)]))

    return rules, page_list


def check_order(rules, pages):
    page_order = {}
    for i, p in enumerate(pages):
        page_order[p] = i
    page_set = set(page_order.keys())
    
    for a, b in rules:
        s = set([a, b])
        if s.issubset(page_set):
            if page_order[a] > page_order[b]:
                return False
    return True


def reassemble_pages(page_order):
    inverted_dict = {}
    for p, i in page_order.items():
        inverted_dict[i] = p
    pages = []
    for k in sorted(inverted_dict.keys()):
        pages.append(inverted_dict[k])
    return pages


def fix_order(rules, pages):
    page_order = {}
    for i, p in enumerate(pages):
        page_order[p] = i
    page_set = set(page_order.keys())
    
    for a, b in rules:
        s = set([a, b])
        if s.issubset(page_set):
            if page_order[a] > page_order[b]:
                new_a_order = page_order[b]
                new_b_order = page_order[a]
                page_order[a] = new_a_order
                page_order[b] = new_b_order
                return fix_order(rules, reassemble_pages(page_order))
                
    return reassemble_pages(page_order)

def sort_rules(rules):
    sorted_rules = []


def part1_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('day05/test_input.txt')
    else:
        puzzle = aoc_library.read_input('day05/input.txt')
    rules, page_list = parse_input(puzzle)
    answer = 0
    for l in page_list:
        result = check_order(rules, l)
        if result:
            answer += l[len(l) // 2]
    return answer



def part2_solve(test=True):
    if test:
        puzzle = aoc_library.read_input('day05/test_input.txt')
    else:
        puzzle = aoc_library.read_input('day05/input.txt')
    rules, page_list = parse_input(puzzle)
    answer = 0
    for l in page_list:
        result = check_order(rules, l)
        if not result:
            corrected_order = fix_order(rules, l)
            answer += corrected_order[len(l) // 2]
    
    return answer


def main():
    # print(f'Part 1 test solution: {part1_solve()}')
    # print(f'Part 1 test solution: {part1_solve(test=False)}')

    print(f'Part 2 test solution: {part2_solve()}')
    print(f'Part 2 test solution: {part2_solve(test=False)}')


if __name__ == "__main__":
    main()
