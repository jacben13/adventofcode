import aoc_library
import copy

class PocketDimension:
    def __init__(self, initial_state):
        self.state = [initial_state]
        self.x = len(initial_state[0])
        self.y = len(initial_state)
        self.z = 1

    def evolve_system(self):
        self.grow_system()
        next_state = copy.deepcopy(self.state)
        # Iterate through self.state and update next_state
        for i in range(self.z):
            for j in range(self.y):
                for k in range(self.x):
                    next_state[i][j][k] = self.check_next_state(k, j, i)

        self.state = next_state
        # self.trim_system()

    def count_active(self):
        active_ = 0
        for slice in self.state:
            for s in slice:
                active_ += sum(s)
        return active_

    def check_next_state(self, x, y, z):
        active_ = 0
        # Check z slice
        if x != 0:
            active_ += self.state[z][y][x - 1]
            active_ += self.state[z][y + 1][x - 1] if y + 1 < self.y else 0
            active_ += self.state[z][y - 1][x - 1] if y > 0 else 0

        active_ += self.state[z][y + 1][x] if y + 1 < self.y else 0
        active_ += self.state[z][y - 1][x] if y > 0 else 0

        if x + 1 < self.x:
            active_ += self.state[z][y][x + 1]
            active_ += self.state[z][y + 1][x + 1] if y + 1 < self.y else 0
            active_ += self.state[z][y - 1][x + 1] if y > 0 else 0

        if active_ > 3:
            return False

        # Check z-1 slice
        if z > 0:
            if x != 0:
                active_ += self.state[z - 1][y][x - 1]
                active_ += self.state[z - 1][y + 1][x - 1] if y + 1 < self.y else 0
                active_ += self.state[z - 1][y - 1][x - 1] if y > 0 else 0

            active_ += self.state[z - 1][y + 1][x] if y + 1 < self.y else 0
            active_ += self.state[z - 1][y][x]
            active_ += self.state[z - 1][y - 1][x] if y > 0 else 0

            if x + 1 < self.x:
                active_ += self.state[z - 1][y][x + 1]
                active_ += self.state[z - 1][y + 1][x + 1] if y + 1 < self.y else 0
                active_ += self.state[z - 1][y - 1][x + 1] if y > 0 else 0

        if active_ > 3:
            return False
        # Check z+1 slice
        if z + 1 < self.z:
            if x != 0:
                active_ += self.state[z + 1][y][x - 1]
                active_ += self.state[z + 1][y + 1][x - 1] if y + 1 < self.y else 0
                active_ += self.state[z + 1][y - 1][x - 1] if y > 0 else 0

            active_ += self.state[z + 1][y + 1][x] if y + 1 < self.y else 0
            active_ += self.state[z + 1][y][x]
            active_ += self.state[z + 1][y - 1][x] if y > 0 else 0

            if x + 1 < self.x:
                active_ += self.state[z + 1][y][x + 1]
                active_ += self.state[z + 1][y + 1][x + 1] if y + 1 < self.y else 0
                active_ += self.state[z + 1][y - 1][x + 1] if y > 0 else 0

        # Change state logic
        my_state = self.state[z][y][x]

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

    def trim_system(self):
        # Trim any rows/columns/slices with no active cubes
        trimmed_state = copy.deepcopy(self.state)

        # Check bottom z layer
        no_trim = False
        for y in trimmed_state[0]:
            no_trim = True in y
            if no_trim:
                break

        if not no_trim:
            del trimmed_state[0]

        # Check top z layer
        no_trim = False
        for y in trimmed_state[-1]:
            no_trim = True in y
            if no_trim:
                break

        if not no_trim:
            del trimmed_state[-1]

        # Check north edge
        no_trim = False
        for z in trimmed_state:
            no_trim = True in z[0]
            if no_trim:
                break
        if not no_trim:
            for i in range(len(trimmed_state)):
                del trimmed_state[i][0]

        # Check south edge
        no_trim = False
        for z in trimmed_state:
            no_trim = True in z[-1]
            if no_trim:
                break
        if not no_trim:
            for i in range(len(trimmed_state)):
                del trimmed_state[i][-1]

        # Check west edge
        no_trim = False
        for z in trimmed_state:
            for y in z:
                no_trim = y[0]
                if no_trim:
                    break
            if no_trim:
                break
        if not no_trim:
            for i in range(len(trimmed_state)):
                for j in range(len(trimmed_state[0])):
                    del trimmed_state[i][j][0]

        # Check east edge
        no_trim = False
        for z in trimmed_state:
            for y in z:
                no_trim = y[-1]
                if no_trim:
                    break
            if no_trim:
                break
        if not no_trim:
            for i in range(len(trimmed_state)):
                for j in range(len(trimmed_state[0])):
                    del trimmed_state[i][j][-1]

        self.state = trimmed_state
        self.z = len(self.state)
        self.y = len(self.state[0])
        self.x = len(self.state[0][0])

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

    def print_system(self, step=0):
        print('Cycle: {}'.format(step))
        for z in gen.state:
            for y in z:
                print(y)
            print('-' * 10)
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
gen.print_system()
for evolution in range(1, evolutions + 1):
    gen.evolve_system()
    gen.print_system(step=evolution)


print('Answer is {}'.format(gen.count_active()))