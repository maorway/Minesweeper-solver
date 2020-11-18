from PIL import Image
from minesweeper.models import Point


def crop(image: Image, start: Point, end: Point):
    return image.crop((*start, *end))