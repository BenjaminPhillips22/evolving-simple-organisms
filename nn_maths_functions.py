from math import atan2
from math import degrees
from math import sqrt


def food_xy_dist(org, food):
    return [food.x-org.x, food.y-org.y]


def dist(org, food):  # x1, y1, x2, y2):
    # return sqrt((x2-x1)**2 + (y2-y1)**2)
    return sqrt((food.x-org.x)**2 + (food.y-org.y)**2)


def calc_heading(org, food):
    d_x = food.x - org.x
    d_y = food.y - org.y
    theta_d = degrees(atan2(d_y, d_x)) - org.r
    if abs(theta_d) > 180: theta_d += 360
    return theta_d / 180
