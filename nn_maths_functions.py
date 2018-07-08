
from numpy import sqrt


def dist(x2, x1, y2, y1):
    return sqrt((x2-x1)**2 + (y2-y1)**2)


def xy_dist(x2, x1, y2, y1):
    return [x2-x1, y2-y1]


def dist_to_food(org, food):
    return dist(food.x, org.x, food.y, org.y)


def xy_dist_to_food(org, food):
    return xy_dist(food.x, org.x, food.y, org.y)


def dist_to_neighbour(org1, org2):
    return dist(org2.x_tail, org1.x, org2.y_tail, org1.y)


def xy_dist_to_neighbour(org1, org2):
    return xy_dist(org2.x_tail, org1.x, org2.y_tail, org1.y)
