# --- IMPORT DEPENDENCIES ------------------------------------------------------+

# from __future__ import division
# from collections import defaultdict

# from matplotlib import pyplot as plt
# from matplotlib.patches import Circle
# import matplotlib.lines as lines

# from plotting import plot_food
# from plotting import plot_organism

import numpy as np
# import operator

# from math import atan2
# from math import cos
# from math import degrees
# from math import floor
# from math import radians
# from math import sin
# from math import sqrt
# from random import randint
# from random import random
# from random import sample
# from random import uniform

import plotting
from organism import Organism
from food import Food
from simulate import simulate
from evolve import evolve
import nn_maths_functions

# --- CONSTANTS --------------------------------------------------------+

settings = {}

# EVOLUTION SETTINGS
settings['pop_size'] = 10       # number of organisms
settings['food_num'] = 10      # number of food particles
settings['gens'] = 5           # number of generations
settings['elitism'] = 0.20      # elitism (selection bias)
settings['mutate'] = 0.10       # mutation rate

# SIMULATION SETTINGS
settings['gen_time'] = 5        # generation length         (seconds)
settings['dt'] = 0.04           # simulation time step      (dt)
settings['dr_max'] = 720        # max rotational speed      (degrees per second)
settings['v_max'] = 0.5         # max velocity              (units per second)
settings['dv_max'] = 0.25      # max acceleration (+/-)    (units per second^2)

settings['x_min'] = -2.0        # arena western border
settings['x_max'] = 2.0        # arena eastern border
settings['y_min'] = -2.0        # arena southern border
settings['y_max'] = 2.0        # arena northern border

settings['plot'] = True         # plot final generation?

# ORGANISM NEURAL NET SETTINGS
settings['inodes'] = 1          # number of input nodes
settings['hnodes'] = 5          # number of hidden nodes
settings['onodes'] = 2          # number of output nodes


def run(settings):

    # --- POPULATE THE ENVIRONMENT WITH FOOD ---------------+
    foods = []
    for i in range(0, settings['food_num']):
        foods.append(Food(settings))

    # --- POPULATE THE ENVIRONMENT WITH ORGANISMS ----------+
    organisms = []
    for i in range(0, settings['pop_size']):
        wih_init = np.random.uniform(-1, 1, (settings['hnodes'], settings['inodes']))     # mlp weights (input -> hidden)
        who_init = np.random.uniform(-1, 1, (settings['onodes'], settings['hnodes']))     # mlp weights (hidden -> output)

        organisms.append(Organism(settings, wih_init, who_init, name='gen[x]-org['+str(i)+']'))

    # --- CYCLE THROUGH EACH GENERATION --------------------+
    for gen in range(0, settings['gens']):

        # SIMULATE
        organisms = simulate(settings, organisms, foods, gen)

        # EVOLVE
        organisms, stats = evolve(settings, organisms, gen)
        print('> GEN:', gen, 'BEST:', stats['BEST'], 'AVG:', stats['AVG'], 'WORST:', stats['WORST'])

    pass


if __name__ == '__main__':
    run(settings)
