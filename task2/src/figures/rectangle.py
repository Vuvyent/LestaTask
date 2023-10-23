from task2.src.figures.figure import Figure
import math
import numpy as np

class Rectangle(Figure):
    def __init__(self, coords):
        self.__type = "Rectangle"
        self.__coords = coords

    @property
    def coords(self):
        return self.__coords

    @coords.setter
    def coords(self, new_coords):
        self.__coords = new_coords

    def _check_validity(self):
        if len(self.coords) != 4:
            raise ValueError('Wrong coordinates! there must be 4 vertices!')
        else:
            for i in range(len(self.coords)):
                if type(self.coords[i]) != tuple and type(self.coords[i]) != list:
                    raise TypeError("vertices of the rectangle must contains in tuple or list")
                if len(self.coords[i]) != 2:
                    raise ValueError('Wrong coordinates! Coordinate of vertex must contain two x,y coordinates')
                for j in range(len(self.coords[i])):
                    if type(self.coords[i][j]) != int and type(self.coords[i][j]) != float:
                        raise TypeError("Coordinates must be integer or float")

        # Rectangle must have 3 pairs of equal elements - parallel sides, and diagonals (2 pairs if square)
        lines = []
        for i in range(len(self.coords)):
            for j in range(len(self.coords)):
                if i != j and i < j:
                    lines.append(math.dist(self.coords[i], self.coords[j]))
        lines = sorted(lines)
        has_no_zero = True
        for i in lines:
            if i == 0:
                has_no_zero = False
                break
        if has_no_zero and lines[0] == lines[1] and lines[2] == lines[3] and lines[4] == lines[5]:
            return
        else:
            raise Exception(f"The points {self.coords} do not form rectangle")

    def draw(self):
        self._check_validity()
        print(f"Drawing Rectangle: vertices in {self.coords[0]}, {self.coords[1]}, {self.coords[2]}, {self.coords[3]}")

