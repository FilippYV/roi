import math
import random
import matplotlib.pyplot as plt


def start(iteration, quantity):
    mass_quantity = []
    for i in range(1, quantity + 1):
        mass_quantity.append(
            [i, round(random.uniform(-10.0, 10.0), 8), round(random.uniform(-10.0, 10.0), 8), 0, 0, 0, 0])
    graph(mass_quantity)
    mass_velosity = []
    # 3 - значение функции на итерации
    # 4 - лучшее значение функций
    # 5 - лучшая x
    # 6 - лучшая y
    # 7 - с крость x
    # 8 - с крость y
    best_value_in_all = [0, 0, 1000000]
    for i in range(iteration):
        print(mass_quantity)
        local_position(mass_quantity)
        global_position(mass_quantity, best_value_in_all)
        print(mass_quantity)
        # print(mass_best_value_in_all)
        velosity(mass_quantity, best_value_in_all)
    print(mass_quantity)
    for i in range(len(mass_quantity)):
        print(f'Частица №{mass_quantity[i][0]}\n'
              f'Функция ({mass_quantity[i][1]}, {mass_quantity[i][2]})'
              f' = {mass_quantity[i][3]}')
    graph_final(mass_quantity)
    graph_final_v2(mass_quantity)


def graph(mass_quantity):
    plt.axis([-10, 10, -10, 10])
    x = []
    y = []
    for i in range(len(mass_quantity)):
        x.append(mass_quantity[i][1])
        y.append(mass_quantity[i][2])
    plt.plot(x, y, 'ro')
    plt.grid()
    plt.savefig('static/start.png')
    plt.close()


def graph_final(mass_quantity):
    plt.axis([-10, 10, -10, 10])
    x = []
    y = []
    for i in range(len(mass_quantity)):
        x.append(mass_quantity[i][1])
        y.append(mass_quantity[i][2])
    plt.plot(x, y, 'ro')
    plt.grid()
    plt.savefig('static/final.png')
    plt.close()


def graph_final_v2(mass_quantity):
    fig = plt.figure()
    x = []
    y = []
    ax = fig.add_subplot()
    for i in range(len(mass_quantity)):
        x.append(mass_quantity[i][1])
        y.append(mass_quantity[i][2])
    ax.scatter(x, y)
    ax.grid()
    plt.savefig('static/final_v2.png')
    plt.close()


def local_position(mass_quantity):
    for i in range(len(mass_quantity)):
        new_best_value_function = round((math.sqrt((mass_quantity[i][1] ** 2 + mass_quantity[1][2] ** 2))), 8)
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
    c_1 = 0.01
    c_2 = 0.01
    r_1 = round(random.uniform(0.0, 1.0), 8)
    r_2 = round(random.uniform(0.0, 1.0), 8)
    for i in range(len(mass_quantity)):
        # print()
        new_v_x = round(mass_quantity[i][-2] + c_1 * r_1 * \
                        (mass_quantity[i][5] - mass_quantity[i][1]) + \
                        c_2 * r_2 * (best_value_in_all[0] - mass_quantity[i][1]), 8)
        new_v_y = round(mass_quantity[i][-1] + c_1 * r_1 * \
                        (mass_quantity[i][6] - mass_quantity[i][2]) + \
                        c_2 * r_2 * (best_value_in_all[1] - mass_quantity[i][2]), 8)
        print(f'{mass_quantity[i][-2]} + {c_1} * {r_1} *'
              f'({mass_quantity[i][5]} - {mass_quantity[i][1]}) + '
              f'{c_2} * {r_2} * ({best_value_in_all[0]} - {mass_quantity[i][1]})')
        print(f'{mass_quantity[i][-1]} + {c_1} * {r_1} *'
              f'({mass_quantity[i][6]} - {mass_quantity[i][2]}) + '
              f'{c_2} * {r_2} * ({best_value_in_all[0]} - {mass_quantity[i][2]})')
        print('Частица - ', i)
        print(f'Новая позиция x = {mass_quantity[i][1]} + {new_v_x} = {round(new_v_x + mass_quantity[i][1], 8)}')
        print(f'Новая позиция y = {mass_quantity[i][2]} + {new_v_y} = {round(new_v_y + mass_quantity[i][2], 8)}')
        mass_quantity[i][1] = round(new_v_x + mass_quantity[i][1], 8)
        mass_quantity[i][2] = round(new_v_y + mass_quantity[i][2], 8)
        print()


def print_first_play(best_value_function, mass_quantity, mass_value_function):
    for i in range(len(mass_quantity)):
        print(f'F(x{mass_quantity[i][0]} : {mass_quantity[i][1]}, '
              f'y{mass_quantity[i][0]} : {mass_quantity[i][2]}) = {mass_value_function[i]}')
    for i in range(len(mass_value_function)):
        if mass_value_function[i] == best_value_function:
            print(f'Лучшее значение функции - F(x{i + 1}, y{i + 1})'
                  f' = {best_value_function}')


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
