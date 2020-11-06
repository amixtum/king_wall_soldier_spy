"""
    utility.py

    utility functions
"""


from random import randrange
from sides import *


def random_direction(l_weight=1, r_weight=1, u_weight=1, d_weight=1):
    l_part = 25 * l_weight
    r_part = 25 * r_weight
    u_part = 25 * u_weight
    d_part = 25 * d_weight

    r = randrange(0, l_part + r_part + u_part + d_part)

    if r <= l_part:
        return LEFT
    
    elif r > l_part and r <= l_part + r_part:
        return RIGHT

    elif r > l_part + r_part and r <= l_part + r_part + u_part:
        return UP
    
    elif r > l_part + r_part + u_part and r <= l_part + r_part + u_part + d_part:
        return DOWN

def direction_to_vector(x, y, direction, max_x, max_y):
    if direction == LEFT:
        if x == 0:
            return None
        return (x - 1, y)
    elif direction == RIGHT:
        if x == max_x - 1:
            return None
        return (x + 1, y)
    elif direction == UP:
        if y == 0:
            return None
        return (x, y - 1)
    elif direction == DOWN:
        if y == max_y - 1:
            return None
        return (x, y + 1)
