"""
    test.py

    testing the game
"""


import os

from game import Game


field_size = int(input("Please enter field size: "))
wall_density = float(input("Please enter wall density (0 <= wall_density <= 1): "))
movement_per_reinforcement = float(input("Please enter number of movements per wave of reinforcements: "))

game = Game(field_size, field_size, wall_density, movement_per_reinforcement)

winner = game.play()

print("Winner is " + winner + "!")