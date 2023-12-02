def read_input(file_name):
    line_list = []
    with open(file_name) as f:
        for line in f:
            line = line.replace('\n', '')
            line_list.append(line)
    return line_list


def read_numbers(file_name):
    line_list = []
    with open(file_name) as f:
        for line in f:
            line = line.replace('\n', '')
            line_list.append(int(line))
    return line_list