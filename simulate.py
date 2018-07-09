
from numpy.random import shuffle

import plotting
import nn_maths_functions
from make_gif import make_gif


def simulate(settings, organisms, foods, gen):

    total_time_steps = settings['time_steps']

    # --- CYCLE THROUGH EACH TIME STEP ---------------------+
    for t_step in range(0, total_time_steps, 1):

        # SHUFFLE ORGANISMS (works inplace)
        # I don't want to favour the orgs at the beginning of the list
        shuffle(organisms)

        # PLOT SIMULATION FRAME
        plot_final_generation = (settings['plot'] is True) and (gen == settings['gens']-1)
        plot_this_generation = (settings['plot'] is True) and (gen in settings['plot_generations'])
        if plot_final_generation or plot_this_generation:
            plotting.plot_frame(settings, organisms, foods, gen, t_step)

        # FOR EACH ORGANISM
        for org1 in organisms:

            # find closest food
            closest_dist_so_far = 10000

            # get the closest food
            for food in foods:

                food_org_dist = nn_maths_functions.dist_to_food(org1, food)

                # update closest food if necessary
                # if food_org_dist < org1.d_food:
                if food_org_dist < closest_dist_so_far:
                    # org1.d_food = food_org_dist
                    closest_dist_so_far = food_org_dist
                    org1.x_distance_to_food, org1.y_distance_to_food = nn_maths_functions.xy_dist_to_food(org1, food)

                # UPDATE FITNESS FUNCTION
                if food_org_dist <= 0.075:
                    org1.fitness += food.energy
                    # SET FOOD AS 'EATEN'
                    food.energy = 0
                    org1.d_food = 10000

            # find closest org
            closest_dist_so_far = 10000

            # get the closest neighbour
            for org2 in organisms:

                if org1 is org2:
                    pass

                org_org_dist = nn_maths_functions.dist_to_neighbour(org1, org2)

                # update closest food if necessary
                if org_org_dist < closest_dist_so_far:
                    closest_dist_so_far = org_org_dist
                    org1.x_distance_to_neighbour, org1.y_distance_to_neighbour = nn_maths_functions.xy_dist_to_neighbour(org1, org2)

                # UPDATE FITNESS FUNCTION
                if org_org_dist <= 0.10:
                    org1.fitness -= 0.1  #

        # GET FOOD RESPONSE
        for food in foods:
            food.respawn(settings)

        # GET ORGANISM RESPONSE
        for org in organisms:
            org.think()

    if plot_final_generation or plot_this_generation:
        make_gif(settings, gen)

    return organisms
