"""
    neighborhood_vectors.py

    utility functions for graph neighborhoods
"""

def adjacent_vectors_neumann(x, y, max_x, max_y):
        adjacent = []
        if x == 0 and y == 0:
            adjacent.append((1, 0))
            adjacent.append((1, 1))
            adjacent.append((0, 1))
        
        elif x == max_x - 1 and y == 0:
            adjacent.append((max_x - 2, 0))
            adjacent.append((max_x - 1, 1))
            adjacent.append((max_x - 1, 1))

        elif x == 0 and y == max_y - 1:
            adjacent.append((1, max_y - 1))
            adjacent.append((1, max_y - 2))
            adjacent.append((0, max_y - 2))

        elif x == max_x - 1 and y == max_y - 1:
            adjacent.append((max_x - 2, max_y - 1))
            adjacent.append((max_x - 1, max_y - 2))
            adjacent.append((max_x - 1, max_y - 2))

        elif x == 0:
            adjacent.append((x, y + 1))
            adjacent.append((x + 1, y + 1))
            adjacent.append((x + 1, y))
            adjacent.append((x + 1, y - 1))
            adjacent.append((x, y - 1))
        
        elif x == max_x - 1:
            adjacent.append((x - 1, y - 1))
            adjacent.append((x - 1, y))
            adjacent.append((x - 1, y + 1))
            adjacent.append((x, y + 1))
            adjacent.append((x, y - 1))

        elif y == 0:
            adjacent.append((x - 1, y))
            adjacent.append((x - 1, y + 1))
            adjacent.append((x, y + 1))
            adjacent.append((x + 1, y + 1))
            adjacent.append((x + 1, y))

        elif y == max_y - 1:
            adjacent.append((x - 1, y - 1))
            adjacent.append((x - 1, y))
            adjacent.append((x + 1, y))
            adjacent.append((x + 1, y - 1))
            adjacent.append((x, y - 1))
        
        else:
            adjacent.append((x - 1, y - 1))
            adjacent.append((x - 1, y))
            adjacent.append((x - 1, y + 1))
            adjacent.append((x, y + 1))
            adjacent.append((x + 1, y + 1))
            adjacent.append((x + 1, y))
            adjacent.append((x + 1, y - 1))
            adjacent.append((x, y - 1))

        return adjacent

def adjacent_vectors_moore(x, y, max_x, max_y):
        adjacent = []
        if x == 0 and y == 0:
            adjacent.append((1, 0))
            adjacent.append((0, 1))
        
        elif x == max_x - 1 and y == 0:
            adjacent.append((max_x - 2, 0))
            adjacent.append((max_x - 1, 1))

        elif x == 0 and y == max_y - 1:
            adjacent.append((1, max_y - 1))
            adjacent.append((0, max_y - 2))

        elif x == max_x - 1 and y == max_y - 1:
            adjacent.append((max_x - 2, max_y - 1))
            adjacent.append((max_x - 1, max_y - 2))

        elif x == 0:
            adjacent.append((x, y + 1))
            adjacent.append((x + 1, y))
            adjacent.append((x, y - 1))
        
        elif x == max_x - 1:
            adjacent.append((x - 1, y))
            adjacent.append((x, y + 1))
            adjacent.append((x, y - 1))

        elif y == 0:
            adjacent.append((x - 1, y))
            adjacent.append((x, y + 1))
            adjacent.append((x + 1, y))

        elif y == max_y - 1:
            adjacent.append((x - 1, y))
            adjacent.append((x + 1, y))
            adjacent.append((x, y - 1))
        
        else:
            adjacent.append((x - 1, y))
            adjacent.append((x, y + 1))
            adjacent.append((x + 1, y))
            adjacent.append((x, y - 1))

        return adjacent