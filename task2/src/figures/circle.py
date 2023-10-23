from task2.src.figures.figure import Figure


class Circle(Figure):
    def __init__(self, center, r):
        self.__type = "Circle"
        self.__center = center
        self.__r = r

    @property
    def center(self):
        return self.__center

    @center.setter
    def center(self, new_center):
        self.__center = new_center

    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self, new_r):
        self.__r = new_r

    def _check_validity(self):
        if type(self.__r) != int and type(self.__r) != float:
            raise TypeError("Radius must be integer or float")
        if self.__r <= 0:
            raise ValueError("Radius must be positive")
        if type(self.__center) != tuple and type(self.__center) != list:
            raise TypeError("Center must be list or tuple")
        if len(self.__center) != 2:
            raise ValueError('Wrong coordinates! Coordinate of vertex must contain two x,y coordinates')
        for i in range(len(self.__center)):
            if type(self.__center[i]) != int and type(self.__center[i]) != float:
                raise TypeError("Coordinates must be integer or float")
        return

    def draw(self):
        self._check_validity()
        print(f"Drawing Circle: center in {self.__center} and radius {self.__r}")
