"""
    test.py

    testing the game
"""


from game import Game

field_size = int(input("Please enter field size: "))
wall_density = float(input("Please enter wall density: "))
movement_per_reinforcement = float(input("Please enter number of movements per wave of reinforcements: "))

game = Game(field_size, wall_density, movement_per_reinforcement)

winner = game.play()

print("Winner is " + winner + "!")