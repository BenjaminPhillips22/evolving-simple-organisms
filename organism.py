
import numpy as np


class Organism():
    def __init__(self, settings, wih=None, who=None, name=None):

        self.velocity_decay_factor = settings['velocity_decay_factor']
        self.max_speed = settings['max_speed']
        self.x_world_size = settings['x_max'] - settings['x_min']
        self.y_world_size = settings['y_max'] - settings['y_min']

        self.x = np.random.uniform(settings['x_min'], settings['x_max'])  # position (x)
        self.y = np.random.uniform(settings['y_min'], settings['y_max'])  # position (y)

        self.x_tail = self.x
        self.y_tail = self.y

        self.x_velocity = 0         # velocity in the x direction
        self.y_velocity = 0         # velocity in the y direction

        self.x_distance_to_food = 0         #
        self.y_distance_to_food = 0         #
        self.d_food = 100                   # distance to nearest food

        self.x_distance_to_neighbour = 0    #
        self.y_distance_to_neighbour = 0    #
        self.d_neighbour = 100              # distance to nearest neighbour

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

        inputs = [
            self.x_velocity,
            self.y_velocity,
            self.x_distance_to_food,
            self.y_distance_to_food,
            self.x_distance_to_neighbour,
            self.y_distance_to_neighbour
        ]
        h1 = af(np.dot(self.wih, inputs))                   # hidden layer
        out = np.multiply(af(np.dot(self.who, h1)), 0.5)    # output layer

        # UPDATE TAIL
        self.x_tail = self.x
        self.y_tail = self.y

        # UPDATE VELOCITIES
        self.x_velocity = float(out[0]) + self.x_velocity*self.velocity_decay_factor
        self.y_velocity = float(out[1]) + self.y_velocity*self.velocity_decay_factor

        # UPDATE POSITION
        self.x += self.x_velocity
        self.y += self.y_velocity
