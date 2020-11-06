"""
    grid.py

    graph container for use in our simulation (see simulation.py)
"""

from vertex import Vertex
from symbols import SPACE, is_soldier, king_symbol
from sides import *
from neighborhood_vectors import adjacent_vectors_moore, adjacent_vectors_neumann

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.vertices = {}
        self.occupied_vertices = {}
        self.spies = {}
        self.soldiers = {}
        self.walls = {}
        self.kings = {}

        for x in range(self.width):
            for y in range(self.height):
                self.vertices[(x, y)] = Vertex((SPACE, None)) # all vertices have the form (text_representation, side)
        
    def soldiers_on_side(self, side):
        if side == LEFT:
            return [s for s in self.soldiers if s.value[1] == LEFT]
        elif side == RIGHT:
            return [s for s in self.soldiers if s.value[1] == RIGHT]
        elif side == UP:
            return [s for s in self.soldiers if s.value[1] == UP]
        elif side == DOWN:
            return [s for s in self.soldiers if s.value[1] == DOWN]

    def spies_on_side(self, side):
        if side == LEFT:
            return [s for s in self.spies if s.value[1] == LEFT]
        elif side == RIGHT:
            return [s for s in self.spies if s.value[1] == RIGHT]
        elif side == UP:
            return [s for s in self.spies if s.value[1] == UP]
        elif side == DOWN:
            return [s for s in self.spies if s.value[1] == DOWN]

    def enemy_soldiers_around_vertex(self, x, y, side):
        return [v for v in self.adjacent_vertices_moore(x, y) if v.value[1] != side and is_soldier(v.value[0])]

    def friendly_soldiers_around_vertex(self, x, y, side):
        return [v for v in self.adjacent_vertices_moore(x, y) if v.value[1] == side and is_soldier(v.value[0])]

    def adjacent_vertices_moore(self, x, y):
        adjacent = adjacent_vectors_moore(x, y, self.width, self.height)
        vs = []

        for vector in adjacent:
            vs.append(self.vertices[vector])

        return vs

    def adjacent_vertices_neumann(self, x, y):
        adjacent = adjacent_vectors_neumann(x, y, self.width, self.height)
        vs = []

        for vector in adjacent:
            vs.append(self.vertices[vector])

        return vs

    def spawn_area_empty(self, side):
        if side == LEFT:
            for y in range(1, self.height - 1):
                unit_here = self.vertices[(0, y)].value[0]
                if unit_here != SPACE and unit_here != king_symbol(side):
                    return False
        elif side == RIGHT:
            for y in range(1, self.height - 1):
                unit_here = self.vertices[(self.width - 1, y)].value[0]
                if unit_here != SPACE and unit_here != king_symbol(side):
                    return False
        elif side == UP:
            for x in range(1, self.width - 1):
                unit_here = self.vertices[(x, 0)].value[0]
                if unit_here != SPACE and unit_here != king_symbol(side):
                    return False
        elif side == DOWN:
            for x in range(1, self.width - 1):
                unit_here = self.vertices[(x, self.height - 1)].value[0]
                if unit_here != SPACE and unit_here != king_symbol(side):
                    return False
        return True

    def spawn_area_full(self, side):
        if side == LEFT:
            for y in range(self.height):
                unit_here = self.vertices[(0, y)].value[0]
                if unit_here == SPACE:
                    return False
        elif side == RIGHT:
            for y in range(self.height):
                unit_here = self.vertices[(self.width - 1, y)].value[0]
                if unit_here == SPACE:
                    return False
        elif side == UP:
            for x in range(self.width):
                unit_here = self.vertices[(x, 0)].value[0]
                if unit_here == SPACE:
                    return False
        elif side == DOWN:
            for x in range(self.width):
                unit_here = self.vertices[(x, self.height - 1)].value[0]
                if unit_here == SPACE:
                    return False
        return True
        
