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


def read_2d(file_name, convert_to_int=False):
    line_list = []
    with open(file_name) as f:
        for line in f:
            line = line.replace('\n', '')
            row = []
            for c in line:
                if convert_to_int:
                    row.append(int(c))
                else:
                    row.append(c)
            line_list.append(row)
    return line_list
