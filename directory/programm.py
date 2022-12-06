import math
import random


def start(iteration, quantity, a, b, y):
    mass_quantity = []
    for i in range(1, quantity + 1):
        mass_quantity.append(
            [i, round(random.uniform(-10.0, 10.0), 4), round(random.uniform(-10.0, 10.0), 4), 0, 0, 0, 0])
    mass_quantity = [[1, -2.5092, 9.0143, 0, 0, 0, 0], [2, -6.8796, -6.8801, 0, 0, 0, 0],
                     [3, 2.0223, 4.1615, 0, 0, 0, 0], [4, 6.6489, -5.7532, 0, 0, 0, 0]]
    mass_velosity = []
    # 3 - значение функции на итерации
    # 4 - лучшее значение функций
    # 5 - лучшая x
    # 6 - лучшая y
    # 7 - с крость x
    # 8 - с крость y
    best_value_in_all = [0, 0, 1000000]
    for i in range(iteration):
        local_position(mass_quantity)
        global_position(mass_quantity, best_value_in_all)
        print(mass_quantity)
        # print(mass_best_value_in_all)
        velosity(mass_quantity, best_value_in_all)
        # print()
        # print(mass_quantity[0][1], mass_quantity[0][2], '\n',
        #       mass_quantity[1][1], mass_quantity[1][2], '\n',
        #       mass_quantity[2][1], mass_quantity[2][2], '\n',
        #       mass_quantity[3][1], mass_quantity[3][2], '\n')


def local_position(mass_quantity):
    for i in range(len(mass_quantity)):
        new_best_value_function = round(2 * math.sin(mass_quantity[i][1] + mass_quantity[i][2] + 10) / \
                                        (math.sqrt(2 * mass_quantity[i][1] ** 2 + mass_quantity[i][2] ** 2 + 0.5)), 4)
        mass_quantity[i][3] = new_best_value_function
        if mass_quantity[i][3] < mass_quantity[i][4]:
            mass_quantity[i][4] = mass_quantity[i][3]
            mass_quantity[i][5] = mass_quantity[i][1]
            mass_quantity[i][6] = mass_quantity[i][2]


def global_position(mass_quantity, best_value_function):
    for i in range(len(mass_quantity)):
        if mass_quantity[i][4] < best_value_function[2]:
            best_value_function = [mass_quantity[i][5], mass_quantity[i][6], mass_quantity[i][4]]


def velosity(mass_quantity, best_value_in_all):
    c_1 = 2
    c_2 = 2
    r_1 = round(random.uniform(0.0, 1.0), 4)
    r_2 = round(random.uniform(0.0, 1.0), 4)
    for i in range(len(mass_quantity)):
        new_v_x = round(mass_quantity[i][-2] + c_1 * r_1 * \
                        (mass_quantity[i][5] - mass_quantity[i][1]) + \
                        c_2 * r_2 * (best_value_in_all[0] - mass_quantity[i][1]), 4)
        new_v_y = round(mass_quantity[i][-1] + c_1 * r_1 * \
                        (mass_quantity[i][6] - mass_quantity[i][2]) + \
                        c_2 * r_2 * (best_value_in_all[1] - mass_quantity[i][2]), 4)
        print(f'По x{i + 1} - vx - ', new_v_x)
        print(f'По y{i + 1} - vy - ', new_v_y)
        print(f'Новая позиция x = {mass_quantity[i][1]} + {new_v_x} = {round(new_v_x + mass_quantity[i][1], 4)}')
        print(f'Новая позиция y = {mass_quantity[i][2]} + {new_v_y} = {round(new_v_y + mass_quantity[i][2], 4)}')
        mass_quantity[i][1] = round(new_v_x + mass_quantity[i][1], 4)
        mass_quantity[i][2] = round(new_v_y + mass_quantity[i][2], 4)


# def new_best(mass_quantity):
#     best_value_function = False
#     mass_value_function = []
#     for i in range(len(mass_quantity)):
#         new_best_value_function = 2 * math.sin(mass_quantity[i][1] + mass_quantity[i][2] + 10) / \
#                                   (math.sqrt(2 * mass_quantity[i][1] ** 2 + mass_quantity[i][2] ** 2 + 0.5))
#         mass_value_function.append(round(new_best_value_function, 4))
#         mass_quantity[i][-2] = mass_value_function[-1]
#         if best_value_function > new_best_value_function:
#             best_value_function = round(new_best_value_function, 4)
#
#     for i in range(len(mass_quantity)):
#         mass_quantity[i][-1] = best_value_function
#     return best_value_function, mass_value_function


def print_first_play(best_value_function, mass_quantity, mass_value_function):
    for i in range(len(mass_quantity)):
        print(f'F(x{mass_quantity[i][0]} : {mass_quantity[i][1]}, '
              f'y{mass_quantity[i][0]} : {mass_quantity[i][2]}) = {mass_value_function[i]}')
    for i in range(len(mass_value_function)):
        if mass_value_function[i] == best_value_function:
            print(f'Лучшее значение функции - F(x{i + 1}, y{i + 1})'
                  f' = {best_value_function}')


def best_position(mass_quantity):
    for i in range(mass_quantity):
        y_t_plus_1 = mass_quantity


def speed_update(mass_quantity):
    print(mass_quantity)
    c_1 = 2
    c_2 = 2
    r_1 = round(random.uniform(0.0, 1.0), 4)
    r_2 = round(random.uniform(0.0, 1.0), 4)
    for i in range(len(mass_quantity)):
        new_v = round(mass_quantity[i][4] + c_1 * r_1 * \
                      (mass_quantity[i][3] - mass_quantity[i][4]) + \
                      c_2 * r_2 * (mass_quantity[i][-1] - mass_quantity[i][4]), 4)
        mass_quantity[i][3] = new_v
        mass_quantity[i][1] = round(mass_quantity[i][1] + new_v, 4)
        mass_quantity[i][2] = round(mass_quantity[i][2] + new_v, 4)
    print(mass_quantity)
    """значения функций это две переменные"""
