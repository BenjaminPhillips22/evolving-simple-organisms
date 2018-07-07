from matplotlib import pyplot as plt
from matplotlib.patches import Circle
import matplotlib.lines as lines

# from math import sin
# from math import cos
# from math import radians

# --- FUNCTIONS -------------------------------------------------------+


def plot_organism(settings, org, ax):

    circle = Circle([org.x, org.y], 0.05, edgecolor='g', facecolor='lightgreen', zorder=8)
    ax.add_artist(circle)

    edge = Circle([org.x, org.y], 0.05, edgecolor='darkgreen', facecolor='None', zorder=8)
    ax.add_artist(edge)

    # tail_len = settings['tail_length']

    # x2 = cos(radians(theta)) * tail_len + x1
    # y2 = sin(radians(theta)) * tail_len + y1

    ax.add_line(lines.Line2D([org.x, org.x_tail], [org.y, org.y_tail], color='darkgreen', linewidth=1, zorder=10))

    pass


def plot_food(food, ax):

    circle = Circle([food.x, food.y], 0.03, edgecolor='darkslateblue', facecolor='mediumslateblue', zorder=5)
    ax.add_artist(circle)

    pass


def plot_frame(settings, organisms, foods, gen, time):
    fig, ax = plt.subplots()
    fig.set_size_inches(9.6, 5.4)
                        
    plt.xlim([settings['x_min'] + settings['x_min'] * 0.25, settings['x_max'] + settings['x_max'] * 0.25])
    plt.ylim([settings['y_min'] + settings['y_min'] * 0.25, settings['y_max'] + settings['y_max'] * 0.25])

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

    plt.savefig(str(gen)+'-'+str(time)+'.png', dpi=80)  # dpi=100 in original
