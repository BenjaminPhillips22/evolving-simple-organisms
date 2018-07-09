from matplotlib import pyplot as plt
from matplotlib.patches import Circle
import matplotlib.lines as lines

# --- FUNCTIONS -------------------------------------------------------+


def plot_organism(settings, org, ax):

    circle = Circle([org.x, org.y], 0.05, edgecolor='g', facecolor='lightgreen', zorder=8)
    ax.add_artist(circle)

    edge = Circle([org.x, org.y], 0.05, edgecolor='darkgreen', facecolor='None', zorder=8)
    ax.add_artist(edge)

    ax.add_line(lines.Line2D([org.x, org.x_tail], [org.y, org.y_tail], color='darkgreen', linewidth=1, zorder=10))

    pass


def plot_food(food, ax):

    circle = Circle([food.x, food.y], 0.03, edgecolor='darkslateblue', facecolor='mediumslateblue', zorder=5)
    ax.add_artist(circle)

    pass


def plot_frame(settings, organisms, foods, gen, time):
    fig, ax = plt.subplots()
    fig.set_size_inches(9.6, 5.4)

    plt.xlim([settings['x_min'] + settings['x_min'] * 0.45, settings['x_max'] + settings['x_max'] * 0.45])
    plt.ylim([settings['y_min'] + settings['y_min'] * 0.45, settings['y_max'] + settings['y_max'] * 0.45])
    # plt.xlim([-10, 10])
    # plt.ylim([-10, 10])

    # PLOT ORGANISMS
    for organism in organisms:
        plot_organism(settings, organism, ax)

    # PLOT FOOD PARTICLES
    for food in foods:
        plot_food(food, ax)

    # MISC PLOT SETTINGS
    ax.set_aspect('equal')
    frame = plt.gca()
    frame.axes.get_xaxis().set_ticks([])
    frame.axes.get_yaxis().set_ticks([])

    plt.figtext(0.025, 0.95, r'GENERATION: '+str(gen))
    plt.figtext(0.025, 0.90, r'T_STEP: '+str(time))

    plt.savefig(str(gen)+'-'+str(time)+'.png', dpi=120)


def plot_stats(settings, gen_stats):
    
    file_name = settings['name'] + settings['datetime'] + '.jpg'

    ng = len(gen_stats)
    
    # get stats
    gens = list(range(ng))
    bests = [gen_stats[i]['BEST'] for i in range(ng)]
    worsts = [gen_stats[i]['WORST'] for i in range(ng)]
    avgs = [gen_stats[i]['AVG'] for i in range(ng)]
    
    fig, ax = plt.subplots()

    ax.plot(gens, bests)
    ax.plot(gens, avgs)
    ax.plot(gens, worsts)

    ax.legend(['Best', 'Average', 'Worst'], loc='upper left')
    ax.set_xlabel('generation')
    ax.set_ylabel('fitness score')

    # SAVE FIGURE
    fig.savefig(file_name, dpi=120)
