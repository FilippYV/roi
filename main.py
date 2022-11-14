from directory.programm import start

if __name__ == '__main__':
    iteration = 1
    quantity = 4
    a = 0.95
    b = 0.2
    y = 0.2
    x = start(iteration, quantity, a, b, y)
    print(x)
