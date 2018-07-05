
import plotting
import nn_maths_functions
from make_gif import make_gif


def simulate(settings, organisms, foods, gen):

    total_time_steps = int(settings['gen_time'] / settings['dt'])

    # --- CYCLE THROUGH EACH TIME STEP ---------------------+
    for t_step in range(0, total_time_steps, 1):

        # PLOT SIMULATION FRAME
        if (settings['plot'] is True) and (gen == settings['gens']-1):
            plotting.plot_frame(settings, organisms, foods, gen, t_step)

        # UPDATE FITNESS FUNCTION
        for food in foods:
            for org in organisms:
                food_org_dist = nn_maths_functions.dist(org.x, org.y, food.x, food.y)

                # UPDATE FITNESS FUNCTION
                if food_org_dist <= 0.075:
                    org.fitness += food.energy
                    food.respawn(settings)

                # RESET DISTANCE AND HEADING TO NEAREST FOOD SOURCE
                org.d_food = 100
                org.r_food = 0

        # CALCULATE HEADING TO NEAREST FOOD SOURCE
        for food in foods:
            for org in organisms:

                # CALCULATE DISTANCE TO SELECTED FOOD PARTICLE
                food_org_dist = nn_maths_functions.dist(org.x, org.y, food.x, food.y)

                # DETERMINE IF THIS IS THE CLOSEST FOOD PARTICLE
                if food_org_dist < org.d_food:
                    org.d_food = food_org_dist
                    org.r_food = nn_maths_functions.calc_heading(org, food)

        # GET ORGANISM RESPONSE
        for org in organisms:
            org.think()

        # UPDATE ORGANISMS POSITION AND VELOCITY
        for org in organisms:
            org.update_r(settings)
            org.update_vel(settings)
            org.update_pos(settings)

    if (settings['plot'] is True) and (gen == settings['gens']-1):
        make_gif(settings)

    return organisms
