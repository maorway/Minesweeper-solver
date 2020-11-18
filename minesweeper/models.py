from dataclasses import dataclass
from enum import Enum


@dataclass
class Point:
    x: int
    y: int

    def __iter__(self):
        return iter([self.x, self.y])

class Cell(Enum):
    UNKNOWN = -1
    EMPTY = 0
