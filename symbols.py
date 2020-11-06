"""
    symbols.py
    symbols for translation to a text representation of the game field
"""


from utility import *
from sides import *


SPACE = "__"

WALL = "||"

LEFT_SOLDIER = "o<"
RIGHT_SOLDIER = ">o"
UP_SOLDIER = "vo"
DOWN_SOLDIER = "o^"

LEFT_SPY = "s-"
RIGHT_SPY = "-s"
UP_SPY = "s+"
DOWN_SPY = "?s"

LEFT_KING = "kl"
RIGHT_KING = "lk"
UP_KING = "k%"
DOWN_KING = "$k"


def is_soldier(symbol):
    if symbol == LEFT_SOLDIER or symbol == RIGHT_SOLDIER or symbol == UP_SOLDIER or symbol == DOWN_SOLDIER:
        return True
    return False

def is_spy(symbol):
    if symbol == LEFT_SPY or symbol == RIGHT_SPY or symbol == UP_SPY or symbol == DOWN_SPY:
        return True
    return False

def is_king(symbol):
    if symbol == LEFT_KING or symbol == RIGHT_KING or symbol == UP_KING or symbol == DOWN_KING:
        return True
    return False

def soldier_symbol(side):
    if side == LEFT:
        return LEFT_SOLDIER
    elif side == RIGHT:
        return RIGHT_SOLDIER
    elif side == UP:
        return UP_SOLDIER
    elif side == DOWN:
        return DOWN_SOLDIER

def spy_symbol(side):
    if side == LEFT:
        return LEFT_SPY
    elif side == RIGHT:
        return RIGHT_SPY
    elif side == UP:
        return UP_SPY
    elif side == DOWN:
        return DOWN_SPY

def king_symbol(side):
    if side == LEFT:
        return LEFT_SPY
    elif side == RIGHT:
        return RIGHT_SPY
    elif side == UP:
        return UP_SPY
    elif side == DOWN:
        return DOWN_SPY
