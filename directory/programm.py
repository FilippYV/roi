import math
import random


def start(iteration, quantity, a, b, y):
    mass_quantity = []
    # for i in range(1, quantity + 1):
    #     mass_quantity.append([i, round(random.uniform(-10.0, 10.0), 4), round(random.uniform(-10.0, 10.0), 4)])
    mass_quantity = [[1, -2.5092, 9.0143], [2, -6.8796, -6.8801], [3, 2.0223, 4.1615], [4, 6.6489, -5.7532]]
    best_value_function, mass_value_function = target_function(mass_quantity)
    print_first_play(best_value_function, mass_quantity, mass_value_function)
    return mass_quantity, best_value_function


def target_function(mass_quantity):
    # F(x, y) = 2⋅sin(𝑥 + 𝑦 + 10) /√2⋅𝑥2 + 𝑦2 + 0.5
    best_value_function = False
    mass_value_function = []
    for i in range(len(mass_quantity)):
        new_best_value_function = 2 * math.sin(mass_quantity[i][1] + mass_quantity[i][2] + 10) / \
                                  (math.sqrt(2 * mass_quantity[i][1] ** 2 + mass_quantity[i][2] ** 2 + 0.5))
        mass_value_function.append(round(new_best_value_function, 4))
        if best_value_function > new_best_value_function:
            best_value_function = round(new_best_value_function, 4)
    return best_value_function, mass_value_function


def print_first_play(best_value_function, mass_quantity, mass_value_function):
    for i in range(len(mass_quantity)):
        print(f'F(x{mass_quantity[i][0]} - {mass_quantity[i][1]}, '
              f'y{mass_quantity[i][0]} - {mass_quantity[i][2]}) = {mass_value_function[i]}')
    for i in range(len(mass_value_function)):
        if mass_value_function[i] == best_value_function:
            print(f'Лучшее значение функции - F(x{i+1}, y{i+1})'
                  f' = {best_value_function}')
