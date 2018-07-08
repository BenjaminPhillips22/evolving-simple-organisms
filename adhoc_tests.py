from random import random
import numpy as np

from organism import Organism
from run import settings

# print(np.dot(np.random.uniform(-1, 1, (5, 4)), [1, 2, 3, 4]))
a, b = [2,3]
print(a)
print(b)
print((8 in []))

organisms = []
for i in range(0, 5):
    wih_init = np.random.uniform(-1, 1, (settings['hnodes'], settings['inodes']))     # mlp weights (input -> hidden)
    who_init = np.random.uniform(-1, 1, (settings['onodes'], settings['hnodes']))     # mlp weights (hidden -> output)

    organisms.append(Organism(settings, wih_init, who_init, name='gen[x]-org['+str(i)+']'))

print(organisms[0])
print(organisms[0].name == organisms[0].name)
print(organisms[0].name == organisms[1].name)
print(organisms[0] is organisms[0])
print(organisms[0] is organisms[1])

print(organisms[0] == organisms[0])
print(organisms[0] == organisms[1])