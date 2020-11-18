from PIL import Image

from minesweeper.image import crop, get_color
from minesweeper.models import Point


class Board:
    def __init__(self, board_size, squares=None):
        self.board_size = board_size
        self.squares = squares

    def __getitem__(self, item):
        return self.squares[item]

    @classmethod
    def from_image(cls, field: Image, board_size, square_size):
        squares = [[0] * board_size for _ in range(board_size)]
        for y in range(0, board_size):
            for x in range(0, board_size):
                start_x = square_size * x
                start_y = square_size * y
                print(x, y)
                squares[x][y] = crop(field, Point(start_x, start_y), Point(start_x + square_size, start_y + square_size))
        return cls(board_size, [[get_color(cell) for cell in row] for row in squares])
