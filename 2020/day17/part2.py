import aoc_library
import copy

class PocketDimension:
    def __init__(self, initial_state):
        self.state = [initial_state]
        self.x = len(initial_state[0])
        self.y = len(initial_state)
        self.z = 1
        self.w = 1

    def evolve_system(self):
        self.grow_system()
        next_state = copy.deepcopy(self.state)
        # Iterate through self.state and update next_state
        for h in range(self.w):
            for i in range(self.z):
                for j in range(self.y):
                    for k in range(self.x):
                        next_state[h][i][j][k] = self.check_next_state(k, j, i, h)

        self.state = next_state
        # self.trim_system()

    def count_active(self):
        active_ = 0
        for slice in self.state:
            for s in slice:
                active_ += sum(s)
        return active_

    def check_next_state(self, x, y, z, w):
        active_ = 0

        # Change state logic
        my_state = self.state[w][z][y][x]

        if active_ > 3:
            return False
        elif my_state and active_ in (2, 3):
            return True
        elif my_state:
            return False
        elif not my_state and active_ == 3:
            return True
        else:
            return False

    def grow_system(self):
        # Add a buffer to each edge
        self.x += 2
        self.y += 2
        self.z += 2
        empty_y_slice = [False for i in range(self.x)]
        empty_z_slice = [copy.deepcopy(empty_y_slice) for i in range(self.y)]
        for s in self.state:
            for x in s:
                x.append(False)
                x.insert(0, False)
            s.append(copy.deepcopy(empty_y_slice))
            s.insert(0, copy.deepcopy(empty_y_slice))
        self.state.append(copy.deepcopy(empty_z_slice))
        self.state.insert(0, copy.deepcopy(empty_z_slice))

    def grow_hypersystem(self):
        self.grow_system()
        empty_y_slice = [False for i in range(self.x)]
        empty_z_slice = [copy.deepcopy(empty_y_slice) for i in range(self.y)]
        empty_cube = [copy.deepcopy(empty_z_slice) for i in range(self.z)]
        self.w += 2



    def print_system(self, step=0):
        print('Cycle: {}'.format(step))
        for w in gen.state
            for z in w:
                for y in z:
                    print(y)
                print('-' * 10)
            print('X' * 10)
        print('*' * 10)



input = aoc_library.read_input('input.txt')
bool_input = []

for y in input:
    slice = []
    for x in y:
        slice.append(x == '#')
    bool_input.append(slice)

gen = PocketDimension(bool_input)

evolutions = 6
# gen.print_system()
for evolution in range(1, evolutions + 1):
    gen.evolve_system()
    # gen.print_system(step=evolution)


print('Answer is {}'.format(gen.count_active()))