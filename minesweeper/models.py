
from enum import Enum, auto


class Point:
    def __init__(self,x: int, y: int = None):
        self.x = x
        self.y = y or x

    def __iter__(self):
        return iter([self.x, self.y])

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y)


class Cell(Enum):
    BOMB = -2
    UNKNOWN = -1
    EMPTY = 0
    ONE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
