from task2.src.figures.figure import Figure
from task2.src.figures.triangle import Triangle
from task2.src.figures.circle import Circle
from task2.src.figures.rectangle import Rectangle


class Engine2D:
    def __init__(self, color=[0, 0, 0]):
        self.__color = color
        self.__canvas = []

    @property
    def color(self):
        return self.__color

    def set_color(self, color):
        if type(color) != list and type(color) != tuple:
            raise TypeError("Color type must be list or tuple")
        if len(color) != 3:
            raise ValueError(f"Len of color is {len(color)}! Color must be presented in RGB-format!")
        for i in range(len(color)):
            if type(color[i]) != int:
                raise TypeError("RGB components must be integer")
            if 0 <= color[i] < 256:
                self.__color = color
            else:
                raise ValueError("RGB must be >=0 and <=255")


    @property
    def canvas(self):
        return self.__canvas

    def add_element(self, figure):
        if type(self.__canvas) != list:
            raise TypeError("Canvas type must be list!")
        if isinstance(figure, Figure):
            self.__canvas.append(figure)
        else:
            raise TypeError(f"figure type is {type(figure)}. figure must be subclass of Figure!")

    def delete_element(self, idx):
        if idx >= len(self.__canvas):
            raise IndexError("Index out of range")
        del(self.__canvas[idx])

    def __clear(self):
        self.__canvas.clear()

    def draw(self):
        for i in self.__canvas:
            print(f"Current color is {self.__color}:", end=" ")
            i.draw()
        self.__clear()
