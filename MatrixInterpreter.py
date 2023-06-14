import time

class MatrixInterpreter:

    count_a = 4
    count_x = 11
    yb = []
    w = []
    u = []
    conditions = []

    def __init__(self, count_y, count_wu, rows_count):
        matrices = self.load_matrices("matrix.txt")

        #self.yb.append(["O" for i in range(self.count_a + self.count_x)])
        for x in range(count_y):
            self.yb.append(matrices[x])

        for x in range(count_y, count_y + count_wu):
            self.w.append(matrices[x])

        for x in range(count_y + count_wu, count_y + count_wu * 2):
            self.u.append(matrices[x])

        self.conditions = [False for i in range(rows_count)]

    def load_matrices(self, path):
        matrices = []

        with open(path) as reader:
            lines = reader.readlines()

            for l in lines:
                pointer = l.find("= ")
                if pointer != -1:
                    matrices.append([])
                    pointer += 2
                    cons = l[pointer:]

                    split_cons = cons.split(" ")
                    for x in range(len(split_cons)):
                        if x % 2 == 0:
                            expression = split_cons[x]
                            row = self.get_row(expression, self.count_a, self.count_x)
                            matrices[-1].append(row)

        return matrices

    def get_row(self, expression, count_a, count_x) -> str:
        row = list('-' * (count_a + count_x))

        bit = '1'
        num = ""
        index = 0
        is_last_digit = False

        for c in expression:
            is_last_digit, index, num, row, bit = self.update_character_of_expression(c,
                                                                                      is_last_digit,
                                                                                      index, num, row, bit)
        is_last_digit, index, num, row, bit = self.update_character_of_expression(' ',
                                                                                  is_last_digit, index, num, row, bit)

        return "".join(row)

    def get_row2(self, s, xb):
        row = format(s, "0" + str(len(self.w)) + "b")
        for x in range(1, len(xb)):
            temp = str(int(xb[x]))
            row += temp
        return row

    def update_character_of_expression(self, c, is_last_digit, index, num, row, bit):
        if not c.isdigit() and is_last_digit:
            index += int(num) - 1
            num = ""
            row[index] = str(bit)
            bit = 1
            is_last_digit = False

        if c == '^':
            bit = '0'

        if c == 'a':
            index = 0

        if c == 'x':
            index = self.count_a

        if c.isdigit():
            num += c
            is_last_digit = True
        else:
            num = ""

        return is_last_digit, index, num, row, bit

    @staticmethod
    def compare_rows(inp, comparator) -> bool:
        is_equal = True
        for x in range(len(inp)):
            if inp[x] != comparator[x] and comparator[x] != '-':
                is_equal = False
                break
        return is_equal

    @staticmethod
    def compare_row_with_matrix(inp, matrix):
        is_equal = False
        for x in range(len(matrix)):
            if MatrixInterpreter.compare_rows(inp, matrix[x]):
                is_equal = True
                break
        return is_equal

    def change_a(self, a, row) -> str:
        for x in range(len(self.w)):
            if MatrixInterpreter.compare_row_with_matrix(row, self.w[x]):
                a[x] = '1'

            if MatrixInterpreter.compare_row_with_matrix(row, self.u[x]):
                a[x] = '0'
        return "".join(a)

    def get_y_str(self, iteration, row) -> str:

        result = "Состояния y(1..15): "

        if iteration == 0:
            result += "-   "
        else:
            found_y = False
            for x in range(len(self.yb)):
                if MatrixInterpreter.compare_row_with_matrix(row, self.yb[x]):
                    found_y = True
                    result += "y" + str(x + 1)
            if found_y:
                result += "   "
            else:
                result += "-   "

        result += "Состояния бинарные y(1..15): "
        if iteration == 0:
            result += "0" * len(self.yb)
        else:
            bin_y = list("0" * len(self.yb))
            for x in range(len(self.yb)):
                bin_y[x] = '1' if MatrixInterpreter.compare_row_with_matrix(row, self.yb[x]) else '0'
            result += "".join(bin_y)

        return result

    def print_state(self, s, row, iteration):
        print("Состояние: S" + str(s) + "   ", end="")
        print("Состояния a(1..4): " + format(s, '04b') + "   ", end="")

        print(self.get_y_str(iteration, row))

        # print("Состояния y(1..15):", end="")
        #
        # for x in range(len(self.yb)):
        #     if MatrixInterpreter.compare_row_with_matrix(row, self.yb[x]):
        #         print(" y" + str(x + 1), end="")
        # print("   ", end="")
        #
        # bin_y = list("0" * len(self.yb))
        # for x in range(len(self.yb)):
        #     bin_y[x] = '1' if MatrixInterpreter.compare_row_with_matrix(row, self.yb[x]) else '0'
        #
        # print("Состояния бинарные y(1..15):" + "".join(bin_y))

    def next_step(self, s, xb):
        row = self.get_row2(s, xb)
        ss = list(format(s, "0" + str(len(self.w)) + "b"))

        return int(self.change_a(ss, row), 2)

    def start(self, xb):
        start = time.time()
        s = 0
        row = ""
        iteration = 0
        while not self.conditions[s]:
            self.conditions[s] = True
            self.print_state(s, row, iteration)
            row = self.get_row2(s, xb)
            s = self.next_step(s, xb)
            iteration += 1

        self.print_state(s, row, iteration)
        row = self.get_row2(s, xb)


        end = time.time()

        elapsed_time = end - start
        elapsed_time_ms = elapsed_time * 1000.0

        if s == 0:
            print("Алгортим завершил работу за ", end="")
        else:
            print("Алгоритм зациклился на состоянии " + str(s) + " за ", end="")


        print(str(elapsed_time_ms) + " миллисекунд.")
