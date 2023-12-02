from aoc_modules import aoc_library

puzzle_input = aoc_library.read_input('input.txt')

class Program():
    def __init__(self, instructions):
        self.program = []
        for i in instructions:
            self.program.append([i, 0])
        self.acc = 0
        self.next = 0

    def parse_instruction(self):
        # print('Current state\nAcc: {}\nNext: {}\nNext instruction: {}'.format(
        #     self.acc, self.next, self.program[self.next][0]))
        if self.next >= len(self.program):
            print('Escaped the loop with acc: {}'.format(self.acc))
            raise EOFError('program exit')
        elif self.program[self.next][1] > 0:
            print('Loop detected, accumulator: {}'.format(self.acc))
            raise RuntimeError('loop')
        next_instruction = self.program[self.next][0].split(' ')
        if next_instruction[0] == 'nop':
            self.program[self.next][1] = 1
            self.next += 1
        elif next_instruction[0] == 'acc':
            self.program[self.next][1] = 1
            self.acc += int(next_instruction[1].replace('+', ''))
            self.next += 1
        elif next_instruction[0] == 'jmp':
            self.program[self.next][1] = 1
            self.next += int(next_instruction[1].replace('+', ''))


gamepad_bl = Program(puzzle_input)

complete = False
mutate_line = 0

for line in puzzle_input:
    if line.split(' ')[0] == 'jmp':
        print('Rewriting jmp to nop on line {}'.format(mutate_line))
        gamepad_bl.program[mutate_line][0] = gamepad_bl.program[mutate_line][0].replace('jmp', 'nop')
    elif line.split(' ')[0] == 'nop':
        print('Rewriting nop to jmp on line {}'.format(mutate_line))
        gamepad_bl.program[mutate_line][0] = gamepad_bl.program[mutate_line][0].replace('nop', 'jmp')
    mutate_line += 1
    print(gamepad_bl.program)
    while not complete:
        try:
            gamepad_bl.parse_instruction()
        except RuntimeError:
            gamepad_bl = Program(puzzle_input)
            break