from task2.src.figures.figure import Figure
import math


class Triangle(Figure):
    def __init__(self, coords):
        self.__type = "Triangle"
        self.__coords = coords

    @property
    def coords(self):
        return self.__coords

    @coords.setter
    def coords(self, new_coords):
        self.__coords = new_coords

    def _check_validity(self):
        if len(self.coords) != 3:
            raise ValueError('Wrong coordinates! There must be 3 vertices!')
        else:
            for i in range(len(self.coords)):
                if type(self.coords[i]) != tuple and type(self.coords[i]) != list:
                    raise TypeError("vertices of the triangle must contains in tuple or list")
                if len(self.coords[i]) != 2:
                    raise ValueError('Wrong coordinates! Coordinate of vertex must contain two x,y coordinates')
                for j in range(len(self.coords[i])):
                    if type(self.coords[i][j]) != int and type(self.coords[i][j]) != float:
                        raise TypeError("Coordinates must be integer or float")

        # belong to one line
        if self.coords[2][0] * (self.coords[1][1] - self.coords[0][1]) - self.coords[2][1] * (self.coords[1][0] -
           self.coords[0][0]) != self.coords[0][0] * self.coords[1][1] - self.coords[1][0] * self.coords[0][1]:
            return
        else:
            raise Exception(f"The points {self.coords} located in one line and do not form Triangle")

    def draw(self):
        self._check_validity()
        print(f"Drawing Triangle: vertices in {self.coords[0]}, {self.coords[1]}, {self.coords[2]}")
