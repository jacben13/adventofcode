def find_seat_row(seat):
    row_chars = seat[:7]
    min = 0
    max = 127
    for char in row_chars:
        delta = max - min + 1
        half = delta // 2
        if char == 'F':
            max -= half
        else:
            min += half
    return min


def find_seat_col(seat):
    col_chars = seat[-3:]
    min = 0
    max = 7
    for char in col_chars:
        delta = max - min + 1
        half = delta // 2
        if char == 'L':
            max -= half
        else:
            min += half
    return min

def calc_seat_id(seat):
    return find_seat_row(seat) * 8 + find_seat_col(seat)

boarding_pass_list = []

with open('input.txt') as f:
    for line in f:
        line = line.replace('\n', '')
        boarding_pass_list.append(line)

max_seat_id = 0
seat_id_list = []
for bp in boarding_pass_list:
    seat_id = calc_seat_id(bp)
    seat_id_list.append(seat_id)
    max_seat_id = max(max_seat_id, seat_id)

seat_id_list.sort()
prev = seat_id_list[0] - 1
for seat in seat_id_list:
    delta = seat - prev
    if delta > 1:
        print('Missing seat id: {}'.format(prev + 1))
    prev = seat