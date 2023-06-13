from LogicInterpreter import LogicInterpreter
from MatrixInterpreter import MatrixInterpreter


def start_matrix_interpreter(x):
    matrix_interpreter = MatrixInterpreter(15, 4, 15)
    matrix_interpreter.start(x)


def start_logic_interpreter(x):
    logic_interpreter = LogicInterpreter(x, 12, 4, 15)
    logic_interpreter.start()


def input_x(x_count) -> []:
    x_count = x_count + 1
    x = [False for i in range(x_count)]

    found_error = False
    while True:
        x_str = str(input("Введите " + str((x_count - 1)) + " x (0 или 1):"))
        x_str_length = len(x_str)

        current_x = 1
        pointer = 0
        while pointer < x_str_length:
            if x_str[pointer] == '0' or x_str[pointer] == '1':
                if current_x >= x_count:
                    print("Вы ввели слишком много значений")
                    found_error = True
                    break
                x[current_x] = x_str[pointer] == '1'
                current_x += 1
            elif x_str[pointer] == ' ':
                pass
            else:
                print("Неверный синтаксис")
                found_error = True
                break

            pointer += 1

        if current_x < x_count - 1:
            print("Вы ввели слишком мало значений")
            found_error = True
        elif current_x == x_count:
            none_of_x1x2x3_is_true = not x[1] and not x[2] and not x[3]
            if none_of_x1x2x3_is_true:
                print("По крайней мере одно из значений x1, x2 и x3 должны быть истинным")
                found_error = True

            x1_and_x2x3_is_true_at_the_same_time = x[1] and (x[2] or x[3])
            if x1_and_x2x3_is_true_at_the_same_time:
                print("Нельзя, чтобы одновременно x1 и x2 или x3 были истинными")
                found_error = True

        if found_error:
            found_error = False
            continue
        break
    return x


def input_answer_about_interpreter() -> str:
    while True:
        print("Выберите способ представления функции:")
        print("    1. Матричный")
        print("    2. Логический")
        print("Ваш ответ:")
        answer = str(input())
        length = len(answer)

        if length > 1:
            print("Неверный синтаксис: вы ввели слишком много значений")
            continue
        elif length <= 0:
            print("Неверный синтаксис: вы ничего не ввели")
            continue

        if answer[0] != '1' and answer[0] != '2':
            print("Неверный синтаксис")
            continue
        break
    return answer


def v13Mili1():
    x = input_x(11)
    answer = input_answer_about_interpreter()

    if answer == '1':
        start_matrix_interpreter(x)
    elif answer == '2':
        start_logic_interpreter(x)


if __name__ == '__main__':

    # logic = LogicInterpreter([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 12, 4, 15)
    #
    # logic.a = [0, 1, 0, 0]
    # logic.y = [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    # logic.print_state_in_line()

    v13Mili1()
