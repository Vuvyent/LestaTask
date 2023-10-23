from abc import ABC, abstractmethod


class Figure(ABC):
    __type = None

    @property
    def type(self):
        return self.__type

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def _check_validity(self):
        pass

    @abstractmethod
    def draw(self):
        pass
