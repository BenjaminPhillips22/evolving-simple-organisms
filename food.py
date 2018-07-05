# from collections import defaultdict

# from matplotlib import pyplot as plt
# from matplotlib.patches import Circle
# import matplotlib.lines as lines

# from plotting import plot_food
# from plotting import plot_organism

# import numpy as np
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
from random import uniform


class Food():
    def __init__(self, settings):
        self.x = uniform(settings['x_min'], settings['x_max'])
        self.y = uniform(settings['y_min'], settings['y_max'])
        self.energy = 1

    def respawn(self, settings):
        self.x = uniform(settings['x_min'], settings['x_max'])
        self.y = uniform(settings['y_min'], settings['y_max'])
        self.energy = 1
