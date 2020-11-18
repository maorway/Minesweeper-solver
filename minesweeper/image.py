from PIL import Image

from minesweeper.config import COLORS
from minesweeper.models import Point, Cell


def crop(image: Image, start: Point, end: Point, diff=0) -> Image:
    start = start - Point(diff)
    end = end + Point(diff)
    return image.crop((*start, *end))


def identify_cell(image: Image) -> Cell:
    colors = image.getcolors()
    colors.sort(key=lambda x: x[0], reverse=True)
    return ([COLORS[i[1]] for i in colors[:5] if i[1] in COLORS] or [Cell.EMPTY])[0]


def get_cell_point(board_point: Point, square_size, start=None) -> Point:
    return Point(square_size * (board_point.x + 0.5) + start.x or 0,
                 square_size * (board_point.y + 0.5) + start.y or 0)
