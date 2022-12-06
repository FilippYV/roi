import numpy as np
import pandas as pd

from collections import Iterable, Counter


class PSO:

    def __init__(self, func, bound, POP_SIZE, w=1, c1=0.2, c2=0.2, v_max=0.05, *, var_name=None):
        bounds = Counter([isinstance(a, Iterable) for a in bound])[True]
        Var_size = int(np.ceil(POP_SIZE ** (1 / bounds)))

        vals = [np.linspace(var[0], var[1], Var_size) if isinstance(var, Iterable) else np.array([var]) for var in
                bound]
        vals = np.array(list(map(lambda var: var.flatten(), np.meshgrid(*vals))))
        self.var_quantity, self.POP_SIZE = vals.shape
        self.func = func
        self.bound = bound
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.v_max = v_max
        self.var_name = var_name

        # Частица
        self.particles = np.array(list(zip(*vals)))

        self.velocity = np.random.rand(*self.particles.shape) * v_max

        # Оптимальное положение частиц
        self.person_best = self.particles.copy()
        # Глобальная оптимальная позиция
        self.global_best = max(self.person_best, key=lambda particle: self.func(*particle)).copy()

    def get_fitness(self):
        return np.array([self.func(*particle) for particle in self.particles])

    def update_position(self):
        for index, particle in enumerate(self.particles):
            V_k_plus_1 = self.w * self.velocity[index] \
                         + self.c1 * np.random.rand() * (self.person_best[index] - particle) \
                         + self.c2 * np.random.rand() * (self.global_best - particle)

            self.particles[index] = self.particles[index] + V_k_plus_1
            self.velocity[index] = V_k_plus_1

            for i, var in enumerate(particle):
                if isinstance(self.bound[i], Iterable):
                    if var < self.bound[i][0]:
                        self.particles[index][i] = self.bound[i][0]
                    elif var > self.bound[i][1]:
                        self.particles[index][i] = self.bound[i][1]
                elif var != self.bound[i]:
                    self.particles[index][i] = self.bound[i]

    def update_best(self):
        global_best_fitness = self.func(*self.global_best)
        person_best_value = np.array([self.func(*particle) for particle in self.person_best])

        for index, particle in enumerate(self.particles):
            current_particle_fitness = self.func(*particle)

            if current_particle_fitness > person_best_value[index]:
                person_best_value[index] = current_particle_fitness
                self.person_best[index] = particle
            if current_particle_fitness > global_best_fitness:
                global_best_fitness = current_particle_fitness
                self.global_best = particle

    def pso(self):
        self.update_position()
        self.update_best()

    def info(self):
        result = pd.DataFrame(self.particles)
        if self.var_name == None:
            result.columns = [f'x{i}' for i in range(len(self.bound))]
        else:
            result.columns = self.var_name
        result['fitness'] = self.get_fitness()
        return result


func = lambda x, y,m: 30 * x - y if x < m and y < m else 30 * y - x if x < m and y >= m else x ** 2 - y / 2 if x >= m and y < m else 20 * (
        y ** 2) - 500 * x
bound = ((0, 60), (0, 60), 30)
var_name = ['x', 'y', 'm']
POP_SIZE = 100
w = 1
c1 = 0.2
c2 = 0.2
v_max = 0.05

pso = PSO(func, bound, POP_SIZE, w, c1, c2, v_max, var_name=var_name)

for _ in range(1000):
    pso.pso()
    print(pso.get_fitness().sum())

print(pso.global_best, func(*pso.global_best))
