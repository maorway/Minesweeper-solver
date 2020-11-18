import itertools
from enum import auto, Enum

from PIL import Image
from minesweeper.models import Point


class Cell(Enum):
    EMPTY = 0
    BLUE = auto()
    GREEN = auto()
    RED = auto()

COLORS = {(0, 0, 255): Cell.BLUE, (0, 123, 0): Cell.GREEN, (255, 0, 0): Cell.RED}


def crop(image: Image, start: Point, end: Point):
    return image.crop((*start, *end))

def get_color(image: Image):
    colors = image.getcolors()
    colors.sort(key=lambda x: x[0], reverse=True)
    return ([COLORS[i[1]] for i in colors[:5] if i[1] in COLORS] or [Cell.EMPTY])[0]
