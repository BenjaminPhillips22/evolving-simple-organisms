
import numpy as np

# from math import cos
# from math import radians
# from math import sin
from random import uniform


class Organism():
    def __init__(self, settings, wih=None, who=None, name=None):

        self.velocity_decay_factor = settings['velocity_decay_factor']

        self.x = uniform(settings['x_min'], settings['x_max'])  # position (x)
        self.y = uniform(settings['y_min'], settings['y_max'])  # position (y)

        self.r = 0  # uniform(0, 360)                 # orientation   [0, 360]
        # self.v = uniform(0, settings['v_max'])   # velocity      [0, v_max]
        # self.dv = uniform(-settings['dv_max'], settings['dv_max'])   # dv

        self.x_velocity = 0         # velocity in the x direction
        self.y_velocity = 0         # velocity in the y direction

        self.d_food = 100   # distance to nearest food
        # self.r_food = 0     # orientation to nearest food

        self.x_distance_to_food = 0
        self.y_distance_to_food = 0

        self.fitness = 0    # fitness (food count)

        self.wih = wih      # weights from input to hidden layer
        self.who = who      # weights from hidden layer to output

        self.name = name

    # NEURAL NETWORK
    def think(self):

        # SIMPLE MLP
        def af(x):
            # activation function
            return np.tanh(x)
        inputs = [self.x_velocity, self.y_velocity, self.x_distance_to_food, self.y_distance_to_food]
        h1 = af(np.dot(self.wih, inputs))  # hidden layer
        out = af(np.dot(self.who, h1))          # output layer

        # UPDATE VELOCITIES
        self.x_velocity = float(out[0]) + self.x_velocity*self.velocity_decay_factor
        self.y_velocity = float(out[1]) + self.y_velocity*self.velocity_decay_factor

        # UPDATE POSITION
        self.x += self.x_velocity
        self.y += self.y_velocity
