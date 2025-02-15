
import numpy as np
import datetime

# import our files.
import plotting
from organism import Organism
from food import Food
from simulate import simulate
from evolve import evolve
import nn_maths_functions
import make_gif

# --- CONSTANTS --------------------------------------------------------+

settings = {}

# FILE DETAILS
settings['name'] = 'the_greatest_show_on_earth'

# EVOLUTION SETTINGS
settings['pop_size'] = 30       # number of organisms
settings['food_num'] = 15      # number of food particles
settings['gens'] = 20           # number of generations
settings['elitism'] = 0.50      # elitism (percent of population to keep and allow to have children)
settings['mutate'] = 0.2     # mutation rate

# SIMULATION SETTINGS
settings['seed'] = 333           # for reproducibility
settings['time_steps'] = 100    # time steps in a generation
settings['x_min'] = -3.0        # arena western border
settings['x_max'] = 3.0        # arena eastern border
settings['y_min'] = -3.0        # arena southern border
settings['y_max'] = 3.0        # arena northern border

# GIF
settings['plot'] = True                         # plot final generation?
# plot these generations as well as the final gen
settings['plot_generations'] = []  # list(range(200, 1000, 100))
settings['gif_fps'] = 12                        # frames per second
settings['datetime'] = datetime.datetime.now().strftime('_%Y-%m-%d_%H-%M-%S')
settings['ts_in_gif'] = settings['time_steps']

# ORGANISM NEURAL NET SETTINGS
settings['velocity_decay_factor'] = 0.12     # velocity decay factor, so the fishies have momentum
settings['inodes'] = 6                      # number of input nodes
settings['hnodes'] = 5                      # number of hidden nodes
settings['onodes'] = 2                      # number of output nodes


def run(settings):

    # --- SET RANDOM SEED ----
    np.random.seed(settings['seed'])

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
    gen_stats = []
    for gen in range(0, settings['gens']):

        # SIMULATE
        organisms = simulate(settings, organisms, foods, gen)

        # EVOLVE
        organisms, stats = evolve(settings, organisms, gen)

        # SAVE GEN STATS
        gen_stats.append(stats)

        print(
            '> GEN:', gen,
            'BEST:', np.round(stats['BEST'], 2),
            'AVG:', np.round(stats['AVG'], 2),
            'WORST:', np.round(stats['WORST'], 2)
            )

    plotting.plot_stats(settings, gen_stats)


if __name__ == '__main__':
    run(settings)
