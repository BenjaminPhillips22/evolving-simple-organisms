import operator

from collections import defaultdict

from math import floor

from numpy.random import randint
from numpy.random import random
from numpy.random import choice
from numpy.random import uniform
from numpy.random import shuffle

from organism import Organism


def evolve(settings, organisms_old, gen):

    elitism_num = int(floor(settings['elitism'] * settings['pop_size']))
    new_orgs = settings['pop_size'] - elitism_num

    # --- GET STATS FROM CURRENT GENERATION ----------------+
    stats = defaultdict(int)
    for org in organisms_old:
        if org.fitness > stats['BEST'] or stats['BEST'] == 0:
            stats['BEST'] = org.fitness

        if org.fitness < stats['WORST'] or stats['WORST'] == 0:
            stats['WORST'] = org.fitness

        stats['SUM'] += org.fitness
        stats['COUNT'] += 1

    stats['AVG'] = stats['SUM'] / stats['COUNT']

    # --- ELITISM (KEEP BEST PERFORMING ORGANISMS) ---------+
    orgs_sorted = sorted(organisms_old, key=operator.attrgetter('fitness'), reverse=True)
    organisms_new = []
    for i in range(0, elitism_num):
        organisms_new.append(Organism(settings, wih=orgs_sorted[i].wih, who=orgs_sorted[i].who, name=orgs_sorted[i].name))

    # --- GENERATE NEW ORGANISMS ---------------------------+
    for w in range(0, new_orgs):

        # SELECTION (TRUNCATION SELECTION)
        canidates = range(0, elitism_num)
        random_index = choice(a=canidates, size=2, replace=False)
        org_1 = orgs_sorted[random_index[0]]
        org_2 = orgs_sorted[random_index[1]]

        # CROSSOVER
        crossover_weight = random()
        wih_new = (crossover_weight * org_1.wih) + ((1 - crossover_weight) * org_2.wih)
        who_new = (crossover_weight * org_1.who) + ((1 - crossover_weight) * org_2.who)
        
        # MUTATION
        mutate = random()
        if mutate <= settings['mutate']:

            # PICK WHICH WEIGHT MATRIX TO MUTATE
            mat_pick = randint(0, 2)

            # MUTATE: WIH WEIGHTS
            if mat_pick == 0:
                index_row = randint(0, settings['hnodes'])
                index_col = randint(0, settings['inodes'])
                wih_new[index_row][index_col] = wih_new[index_row][index_col] * uniform(0.9, 1.1)

            # MUTATE: WHO WEIGHTS
            if mat_pick == 1:
                index_row = randint(0, settings['onodes'])
                index_col = randint(0, settings['hnodes'])
                who_new[index_row][index_col] = who_new[index_row][index_col] * uniform(0.9, 1.1)

        organisms_new.append(Organism(settings, wih=wih_new, who=who_new, name='gen['+str(gen)+']-org['+str(w)+']'))

    # SHUFFLE ORGANISMS (this may be needed depending on future edits to fitness)
    # works inplace
    shuffle(organisms_new)

    return organisms_new, stats
