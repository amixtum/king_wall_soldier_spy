"""
    simulation.py

    Objective: capture the King
    Soldier vs Soldier: 50/50
    2 Soldier vs Spy: Turn Spy
    Spy vs Soldier: Turn Soldier
    Walls are impassable
"""


from random import randrange
from random import choice
from random import random

from grid import Grid
from symbols import WALL, SPACE, is_soldier, is_spy, is_king, soldier_symbol, spy_symbol, king_symbol
from sides import LEFT, RIGHT, UP, DOWN
from neighborhood_vectors import adjacent_vectors_moore
from utility import random_direction, direction_to_vector


class Game:
    def __init__(self, size, wall_density, movement_per_reinforcement):
        self.grid = Grid(size, size)
        self.sides = [LEFT, RIGHT, UP, DOWN]
        self.winner = None
        self.left_forward_speed = 1
        self.right_forward_speed = 1
        self.up_forward_speed = 1
        self.down_forward_speed = 1
        self.left_soldier_density = 0.25
        self.right_soldier_density = 0.25
        self.up_soldier_density = 0.25
        self.down_soldier_density = 0.25
        self.movement_per_reinforcement = int(movement_per_reinforcement)
        self.soldiers_spawn_next = True

        self.spawn_walls(wall_density, 0)


    def play(self):
        self.left_soldier_density = float(input("LEFT: Enter soldier density in range (0, 0.5): "))
        self.left_forward_speed = float(input("LEFT: Enter forward speed in range (0, 4): "))

        self.right_soldier_density = float(input("RIGHT: Enter soldier density in range (0, 0.5): "))
        self.right_forward_speed = float(input("RIGHT: Enter forward speed in range (0, 4): "))

        self.up_soldier_density = float(input("UP: Enter soldier density in range (0, 0.5): "))
        self.up_forward_speed = float(input("UP: Enter forward speed in range (0, 4): "))

        self.down_soldier_density = float(input("DOWN: Enter soldier density in range (0, 0.5): "))
        self.down_forward_speed = float(input("DOWN: Enter forward speed in range (0, 4): "))

        self.__spawn_king(0, int(self.grid.height / 2), LEFT)
        self.__spawn_king(self.grid.width - 1, int(self.grid.height / 2), RIGHT)
        self.__spawn_king(int(self.grid.width / 2), 0, UP)
        self.__spawn_king(int(self.grid.width / 2), self.grid.height - 1, DOWN)


        print(self)

        while self.winner is None:
            # spawn reinforcements
            self.spawn_units()

            # display the state of the game
            print(self)

            # prompt user input to continue
            # input("Press Enter/Return to continue")

            # process movement
            for _ in range(self.movement_per_reinforcement):
                    next_side = choice(self.sides)
                    self.move_soldiers(next_side, self.__forward_strength(next_side))

                    next_side = choice(self.sides)
                    self.move_spies(next_side, self.__forward_strength(next_side))
                
        return self.winner

    def spawn_units(self):
        if self.soldiers_spawn_next:
            self.spawn_soldiers(LEFT, self.left_soldier_density)
            self.spawn_soldiers(RIGHT, self.right_soldier_density)
            self.spawn_soldiers(UP, self.up_soldier_density)
            self.spawn_soldiers(DOWN, self.down_soldier_density)

        else:
            self.spawn_spies(LEFT, 0.5 - self.left_soldier_density)
            self.spawn_spies(RIGHT, 0.5 - self.right_soldier_density)
            self.spawn_spies(UP, 0.5 - self.up_soldier_density)
            self.spawn_spies(DOWN, 0.5 - self.down_soldier_density)

    def spawn_soldiers(self, side, density):
        if self.grid.spawn_area_empty(side):
            self.soldiers_spawn_next = False
            if side == LEFT:
                N = int(density * self.grid.height)
                x = 0

                for _ in range(N):
                    y = randrange(1, self.grid.height - 1)
                    while (x, y) in self.grid.occupied_vertices.keys():
                        y = randrange(1, self.grid.height - 1)
                    
                    self.__spawn_soldier(x, y, side)
            elif side == RIGHT:
                N = int(density * self.grid.height)
                x = self.grid.width - 1

                for _ in range(N):
                    y = randrange(1, self.grid.height - 1)
                    while (x, y) in self.grid.occupied_vertices.keys():
                        y = randrange(1, self.grid.height - 1)
                    
                    self.__spawn_soldier(x, y, side)
            elif side == UP:
                N = int(density * self.grid.width)
                y = 0

                for _ in range(N):
                    x = randrange(1, self.grid.width - 1)
                    while (x, y) in self.grid.occupied_vertices.keys():
                        x = randrange(1, self.grid.width - 1)
                    
                    self.__spawn_soldier(x, y, side)
            elif side == DOWN:
                N = int(density * self.grid.width)
                y = self.grid.height - 1

                for _ in range(N):
                    x = randrange(1, self.grid.width - 1)
                    while (x, y) in self.grid.occupied_vertices.keys():
                        x = randrange(1, self.grid.width - 1)
                    
                    self.__spawn_soldier(x, y, side)

    def spawn_spies(self, side, density):
        if self.grid.spawn_area_empty(side):
            self.soldiers_spawn_next = True
            if side == LEFT:
                N = int(density * self.grid.height)
                x = 0

                for _ in range(N):
                    y = randrange(1, self.grid.height - 1)
                    while (x, y) in self.grid.occupied_vertices.keys():
                        y = randrange(1, self.grid.height - 1)
                    
                    self.__spawn_spy(x, y, side)
            elif side == RIGHT:
                N = int(density * self.grid.height)
                x = self.grid.width - 1

                for _ in range(N):
                    y = randrange(1, self.grid.height - 1)
                    while (x, y) in self.grid.occupied_vertices.keys():
                        y = randrange(0, self.grid.height)
                    
                    self.__spawn_spy(x, y, side)
            elif side == UP:
                N = int(density * self.grid.width)
                y = 0

                for _ in range(N):
                    x = randrange(1, self.grid.width - 1)
                    while (x, y) in self.grid.occupied_vertices.keys():
                        x = randrange(1, self.grid.width - 1)
                    
                    self.__spawn_spy(x, y, side)
            elif side == DOWN:
                N = int(density * self.grid.width)
                y = self.grid.height - 1

                for _ in range(N):
                    x = randrange(1, self.grid.width - 1)
                    while (x, y) in self.grid.occupied_vertices.keys():
                        x = randrange(1, self.grid.width - 1)
                    
                    self.__spawn_spy(x, y, side)

    # 0 <= density <= 1
    def spawn_walls(self, density, outer_rim):
        for x in range(outer_rim, self.grid.width - outer_rim):
            for y in range(outer_rim, self.grid.height - outer_rim):
                r = random()
                if r < density:
                    self.__spawn_wall(x, y)

    # 0 <= forward strength <= 4
    def move_soldiers(self, side, forward_strength):
        for position_and_vertex in [item for item in self.grid.soldiers.items() if item[1].value[1] == side]:
            position = position_and_vertex[0]
            direction = None

            if side == LEFT:
                direction = random_direction(r_weight=forward_strength)
            elif side == RIGHT:
                direction = random_direction(l_weight=forward_strength)
            elif side == UP:
                direction = random_direction(d_weight=forward_strength)
            elif side == DOWN:
                direction = random_direction(u_weight=forward_strength)

            self.move_soldier(position[0], position[1], direction, side)

    # 0 <= forward strength <= 4
    def move_spies(self, side, forward_strength):
        for position_and_vertex in [item for item in self.grid.spies.items() if item[1].value[1] == side]:
            direction = None
            next_position = None
            valid_move = False
            turned_soldier = False
            turned_spy = False
            max_attempts = 3
            attempts = 0

            # keep iterating until we find a valid move
            while not valid_move:
                attempts += 1
                if side == LEFT:
                    direction = random_direction(r_weight=forward_strength)
                elif side == RIGHT:
                    direction = random_direction(l_weight=forward_strength)
                elif side == UP:
                    direction = random_direction(d_weight=forward_strength)
                elif side == DOWN:
                    direction = random_direction(u_weight=forward_strength)

                position = (position_and_vertex[0][0], position_and_vertex[0][1])
                next_position = direction_to_vector(position[0], position[1], direction, self.grid.width, self.grid.height)
                if next_position is None:
                    continue

                vertex_at_next_position = self.grid.vertices[next_position]
                unit_type = vertex_at_next_position.value[0]
                unit_side = vertex_at_next_position.value[1]

                enemy_soldiers_around_vertex = self.grid.enemy_soldiers_around_vertex(next_position[0], next_position[1], side)

                # quit trying to avoid an infinite loop *****HACK*****
                if attempts > max_attempts:
                    return

                # check if the move is valid. if it is, we're moving the spy, and continuing to the next one
                if unit_type != WALL and not is_spy(unit_type) and unit_side != side:
                    valid_move = True

                    # check if the spy is interacting with a soldier
                    if is_soldier(unit_type):

                        # destroy the spy if there is more than one soldier around the soldier the spy is interacting with
                        if len(enemy_soldiers_around_vertex) >= 1:
                            turned_spy = True

                        # turn the soldier if there are no adjacent soldiers around it
                        else:
                            turned_soldier = True

                    # check if there is a king at that position
                    # if so, the side who found the king wins
                    elif is_king(unit_type):
                        self.winner = side
                        return
            
            if turned_soldier:
                vertex_at_next_position.value = (soldier_symbol(side), side)
            elif turned_spy:
                self.__destroy_spy(position[0], position[1])
            else:
                self.__transfer_unit(position[0], position[1], direction)
                self.grid.spies.pop((position[0], position[1]))
                self.grid.spies[next_position] = vertex_at_next_position

    def move_soldier(self, x, y, direction, side):
        soldier = self.grid.vertices[(x, y)]

        next_position = direction_to_vector(x, y, direction, self.grid.width, self.grid.height)
        if next_position is None:
            return False

        next_vertex = self.grid.vertices[next_position]
        unit_type = next_vertex.value[0]
        unit_side = next_vertex.value[1]

        if unit_side == side:
            return False

        # check if there is an empty space to move into
        elif unit_type == SPACE:
            self.__transfer_unit(x, y, direction)
            self.grid.soldiers.pop((x, y))
            self.grid.soldiers[next_position] = next_vertex
            return True

        # if not, check if there is a wall blocking the way
        elif unit_type == WALL:
            return False

        # if not, check if there is another soldier there to fight with
        elif is_soldier(unit_type):
            winner = random()

            # this soldier wins
            if winner < 0.5:
                next_vertex.value = (SPACE, None)
                self.grid.soldiers.pop(next_position)
                self.grid.occupied_vertices.pop(next_position)

            # enemy soldier wins
            else:
                soldier.value = (SPACE, None)
                self.grid.soldiers.pop((x, y))
                self.grid.occupied_vertices.pop((x, y))
            return True

        # if there is a spy there, check if there is at least one nearby soldier to turn the spy
        elif is_spy(unit_type):
            nearby_friendly_soldiers = len(self.grid.friendly_soldiers_around_vertex(x, y, side))
            if nearby_friendly_soldiers > 0:
                next_vertex.value = (spy_symbol(side), side)
        # if not, this soldier gets turned by the spy
            else:
                soldier.value = (unit_type, unit_side)

    def __destroy_soldier(self, x, y):
        self.grid.occupied_vertices.pop((x, y))
        self.grid.soldiers.pop((x, y))
        self.grid.vertices[(x, y)] = (SPACE, None)

    def __destroy_spy(self, x, y):
        self.grid.occupied_vertices.pop((x, y))
        self.grid.spies.pop((x, y))
        self.grid.vertices[(x, y)] = (SPACE, None)

    def __spawn_soldier(self, x, y, side):
        self.grid.vertices[(x, y)].value = (soldier_symbol(side), side)
        self.grid.soldiers[(x, y)] = (self.grid.vertices[(x, y)])
        self.grid.occupied_vertices[(x, y)] = self.grid.vertices[(x, y)]

    def __spawn_spy(self, x, y, side):
        self.grid.vertices[(x, y)].value = (spy_symbol(side), side)
        self.grid.spies[(x, y)] = (self.grid.vertices[(x, y)])
        self.grid.occupied_vertices[(x, y)] = self.grid.vertices[(x, y)]

    def __spawn_king(self, x, y, side):
        self.grid.vertices[(x, y)].value = (king_symbol(side), side)
        self.grid.occupied_vertices[(x, y)] = self.grid.vertices[(x, y)]
        self.grid.kings[(x, y)] = self.grid.vertices[(x, y)]

    def __spawn_wall(self, x, y):
        self.grid.vertices[(x, y)].value = (WALL, None)
        self.grid.occupied_vertices[(x, y)] = self.grid.vertices[(x, y)]
        self.grid.walls[(x, y)] = self.grid.vertices[(x, y)]

    def __transfer_unit(self, from_x, from_y, direction):
        from_vertex = self.grid.vertices[(from_x, from_y)]
        next_vertex_position = direction_to_vector(from_x, from_y, direction, self.grid.width, self.grid.height)
        to_vertex = self.grid.vertices[next_vertex_position]
        to_vertex.value = (from_vertex.value[0], from_vertex.value[1])
        from_vertex.value = (SPACE, None)
        self.grid.occupied_vertices.pop((from_x, from_y))
        self.grid.occupied_vertices[next_vertex_position] = to_vertex
        if from_vertex.previsit is not None:
            to_vertex.previsit = from_vertex.previsit
            from_vertex.previsit = None

    def __forward_strength(self, side):
        if side == LEFT:
            return self.left_forward_speed
        elif side == RIGHT:
            return self.right_forward_speed
        elif side == UP:
            return self.up_forward_speed
        elif side == DOWN:
            return self.down_forward_speed
        return None

    def __str__(self):
        out = ""
        for y in range(self.grid.height):
            for x in range(self.grid.width):
                symbol = self.grid.vertices[(x, y)].value[0]
                out += symbol
            out += "\n"
        return out
