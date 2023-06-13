import time

class LogicInterpreter:
    a = []
    y = []
    x = []
    w = []
    u = []
    conditions = []

    def __init__(self, x, states_count, code_size, y_count):
        self.a = [False for i in range(code_size + 1)]
        self.w = [False for i in range(code_size + 1)]
        self.u = [False for i in range(code_size + 1)]
        self.conditions = [False for i in range(states_count + 1)]

        self.y = [False for i in range(y_count + 1)]
        self.x = x

    def update_y(self):
        a = self.a
        x = self.x
        self.y[1] = not a[1] and not a[2] and not a[3] and not a[4] and x[1] or not a[1] and not a[2] and not a[
            3] and not a[4] and (x[3] or x[2])

        self.y[2] = not a[1] and not a[2] and not a[3] and a[4] and x[1]

        self.y[3] = not a[1] and not a[2] and a[3] and not a[4] and (x[3] or x[2])

        self.y[4] = not a[1] and not a[2] and a[3] and not a[4] and (x[3] or x[2]) or not a[1] and a[2] and a[3] and a[4] and x[4]

        self.y[5] = not a[1] and a[2] and a[3] and not a[4] or a[1] and not a[2] and not a[3] and not a[4] and not x[6]

        self.y[6] = not a[1] and a[2] and a[3] and a[4] and x[4] or a[1] and not a[2] and not a[3] and a[4]

        self.y[7] = not a[1] and not a[2] and a[3] and a[4] and x[5] or a[1] and not a[2] and not a[3] and not a[4] and x[6]

        self.y[8] = not a[1] and a[2] and not a[3] and not a[4]

        self.y[9] = not a[1] and a[2] and not a[3] and not a[4]

        self.y[10] = not a[1] and a[2] and not a[3] and not a[4] or a[1] and not a[2] and not a[3] and a[4]

        self.y[11] = a[1] and not a[2] and not a[3] and a[4]

        self.y[12] = not a[1] and a[2] and not a[3] and a[4] and x[7] and not x[2] and x[4] or a[1] and not a[2] and a[
            3] and not a[4] and x[7]

        self.y[13] = not a[1] and a[2] and not a[3] and a[4] and x[7] and x[2] and x[9] or a[1] and not a[2] and a[
            3] and a[4] and x[1] and x[8] or a[1] and not a[2] and a[3] and a[4] and not x[1] and x[2] and x[9]

        self.y[14] = a[1] and a[2] and not a[3] and not a[4] and (x[10] and not x[11] or not x[10] and x[11])

        self.y[15] = not a[1] and a[2] and not a[3] and a[4] and x[7] and not x[2] and not x[4] or not a[1] and a[2] and a[3] and a[4] and not x[4]

    def update_w(self):
        a = self.a
        x = self.x
        self.w[1] = not a[1] and a[2] and not a[3] and a[4] and x[7] and not x[2] and x[4] or not a[1] and a[2] and not \
        a[3] and a[4] and x[7] and x[2] and x[9] or not a[1] and a[2] and not a[3] and a[4] and x[7] and x[2] and not x[
            9] or not a[1] and a[2] and a[3] and a[4] and x[4]

        self.w[2] = not a[1] and not a[2] and not a[3] and a[4] and x[1] or not a[1] and not a[2] and a[3] and a[4] and \
                    x[5] or not a[1] and not a[2] and a[3] and a[4] and not x[5] or a[1] and not a[2] and a[3] and a[
                        4] and x[1] and x[8] or a[1] and not a[2] and a[3] and a[4] and x[1] and not x[8] or a[
                        1] and not a[2] and a[3] and a[4] and not x[1] and x[2] and x[9] or a[1] and not a[2] and a[
                        3] and a[4] and not x[1] and x[2] and not x[9] or a[1] and not a[2] and a[3] and a[4] and not x[
            1] and not x[2]

        self.w[3] = not a[1] and not a[2] and not a[3] and not a[4] and (x[3] or x[2]) or not a[1] and not a[2] and not a[3] and a[4] and x[1] or not a[1] and a[2] and not a[3] and a[4] and not x[
            7] or not a[1] and a[2] and not a[3] and a[4] and x[7] and not x[2] and x[4] or a[1] and not a[2] and not a[
            3] and a[4]

        self.w[4] = not a[1] and not a[2] and not a[3] and not a[4] and x[1] or not a[1] and not a[2] and a[3] and not a[4] and (x[3] or x[2]) or not a[1] and a[2] and not a[3] and not a[4] or not a[1] and a[2] and a[3] and not a[4] or a[1] and not a[
            2] and not a[3] and not a[4] and x[6] or a[1] and not a[2] and not a[3] and not a[4] and not x[6] or a[
            1] and not a[2] and a[3] and not a[4] and x[7]

    def update_u(self):
        a = self.a
        x = self.x
        self.u[1] = a[1] and a[2] and not a[3] and not a[4] and (x[10] and not x[11] or not x[10] and x[11]) or a[1] and a[2] and not a[3] and not a[4] and not (x[10] and not x[11] or not x[10] and x[11])
        self.u[2] = not a[1] and a[2] and not a[3] and a[4] and not x[7] or not a[1] and a[2] and not a[3] and a[4] and x[7] and not x[2] and x[4] or not a[1] and a[2] and not a[3] and a[4] and x[7] and not x[2] and not x[4] or not a[1] and a[2] and a[3] and a[4] and x[4] or not a[1] and a[2] and a[3] and a[4] and not x[4] or a[1] and a[2] and not a[3] and not a[4] and (x[10] and not x[11] or not x[10] and x[11]) or a[1] and a[2] and not a[3] and not a[4] and not (x[10] and not x[11] or not x[10] and x[11])
        self.u[3] = not a[1] and not a[2] and a[3] and a[4] and x[5] or not a[1] and not a[2] and a[3] and a[4] and not x[5] or not a[1] and a[2] and a[3] and a[4] and x[4] or not a[1] and a[2] and a[3] and a[4] and not x[4] or a[1] and not a[2] and a[3] and not a[4] and not x[7] or a[1] and not a[2] and a[3] and a[4] and x[1] and x[8] or a[1] and not a[2] and a[3] and a[4] and x[1] and not x[8] or a[1] and not a[2] and a[3] and a[4] and not x[1] and x[2] and x[9] or a[1] and not a[2] and a[3] and a[4] and not x[1] and x[2] and not x[9] or a[1] and not a[2] and a[3] and a[4] and not x[1] and not x[2]
        self.u[4] = not a[1] and not a[2] and not a[3] and a[4] and x[1] or not a[1] and not a[2] and a[3] and a[4] and x[5] or not a[1] and not a[2] and a[3] and a[4] and not x[5] or not a[1] and a[2] and not a[3] and a[4] and x[7] and not x[2] and not x[4] or not a[1] and a[2] and not a[3] and a[4] and x[7] and x[2] and x[9] or not a[1] and a[2] and not a[3] and a[4] and x[7] and x[2] and not x[9] or not a[1] and a[2] and a[3] and a[4] and x[4] or not a[1] and a[2] and a[3] and a[4] and not x[4] or a[1] and not a[2] and not a[3] and a[4] or a[1] and not a[2] and a[3] and a[4] and x[1] and x[8] or a[1] and not a[2] and a[3] and a[4] and x[1] and not x[8] or a[1] and not a[2] and a[3] and a[4] and not x[1] and x[2] and x[9] or a[1] and not a[2] and a[3] and a[4] and not x[1] and x[2] and not x[9] or a[1] and not a[2] and a[3] and a[4] and not x[1] and not x[2]

    def change_a(self):
        for i in range(1, len(self.a)):
            if self.w[i]:
                self.a[i] = True

            if self.u[i]:
                self.a[i] = False

    @staticmethod
    def to_dec(binary_array) -> int:
        result = 0
        binary_array_length = len(binary_array)
        for i in range(binary_array_length - 1, -1, -1):
            value1 = (1 if binary_array[i] else 0)
            value2 = pow(2.0, binary_array_length - 1 - i)
            result += value1 * value2
        return int(result)

    @staticmethod
    def out(binary_array) -> str:
        out_str = ""
        for bit in binary_array:
            out_str += str(int(bit))
        return out_str

    def next_step(self):
        self.update_y()
        self.update_w()
        self.update_u()
        self.change_a()

    def print_state_in_line(self):
        state = self.to_dec(self.a)
        print("Состояние: S" + str(state) + "   ", end="")
        print("Состояния a(1..4): " + self.out(self.a) + "   ", end="")
        print("Состояния y(1..15): ", end="")

        found_y = False
        for i in range(len(self.y) - 1):
            if self.y[i + 1]:
                found_y = True
                print("y" + str((i + 1)), end="")
        if found_y:
            print("   ", end="")

        if not found_y:
            print("-   ", end="")

        print("Бинарное состояние y(1..15): ", end="")
        for i in range(1, len(self.y)):
            if self.y[i]:
                print("1", end="")
            else:
                print("0", end="")
        print("")

    def start(self):

        start = time.time()

        state = self.to_dec(self.a)
        while not self.conditions[state]:
            self.conditions[state] = True
            self.print_state_in_line()
            self.next_step()
            state = self.to_dec(self.a)

        self.print_state_in_line()

        end = time.time()

        elapsed_time = end - start
        elapsed_time_ms = elapsed_time * 1000.0

        if state == 0:
            print("Алгортим завершил работу за ", end="")
        else:
            print("Алгоритм зациклился на состоянии за ", end="")

        print(str(elapsed_time_ms) + " миллисекунд.")
