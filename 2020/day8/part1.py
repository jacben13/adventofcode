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
        if self.program[self.next][1] > 0:
            print('Loop detected, accumulator: {}'.format(self.acc))
            raise Exception('loop')
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

while True:
    gamepad_bl.parse_instruction()