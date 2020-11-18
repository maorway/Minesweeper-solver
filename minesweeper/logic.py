from PIL import Image

from minesweeper.config import CROP_DIFF
from minesweeper.controls import mouse_click
from minesweeper.image import crop, identify_cell, get_cell_point
from minesweeper.models import Point, Cell

SURROUNDING = ((-1, -1), (-1, 0), (-1, 1),
               (0, -1), (0, 1),
               (1, -1), (1, 0), (1, 1))


class Board:
    def __init__(self, board_size, start: Point, squares=None):
        self.size = board_size
        self.squares = squares
        self.start = start

    def __getitem__(self, item):
        return self.squares[item]

    @classmethod
    def from_image(cls, field: Image, start, board_size, square_size):
        squares = [[0] * board_size for _ in range(board_size)]
        for y in range(0, board_size):
            for x in range(0, board_size):
                start = Point(square_size * x, square_size * y)
                squares[x][y] = crop(field, start, start + Point(square_size), diff=CROP_DIFF)
        return cls(board_size, start, [[identify_cell(cell) for cell in row] for row in squares])

    def basic_strategy(self):
        """
        find 1 cells, if has one unknown is bomb.
        :return:
        """
        for x, col in enumerate(self.squares):
            for y, cell in enumerate(col):
                if cell == Cell.ONE:
                    surrounding = self.surrounding_cells(Point(x, y))
                    if len(surrounding) == 1:
                        x, y, value = surrounding[0]
                        self.squares[x][y] = Cell.BOMB
                        self.click(Point(x, y), self.size, right=True)


    def surrounding_cells(self, point: Point, value_filter=lambda x: True):
        wanted = []
        for x, y in SURROUNDING:
            check_x = point.x + x
            check_y = point.y + y
            value = self[check_x][check_y]
            if value_filter(value):
                wanted.append((check_x, check_y, value))
            return wanted

    def click(self, point: Point, right=False):
        return mouse_click(get_cell_point(point, self.size, start=self.start), right)