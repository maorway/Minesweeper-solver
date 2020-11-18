"""
Solve minesweeper in http://minesweeperonline.com/#beginner
"""
from PIL import Image

from minesweeper.config import START, END, BOARD_SIZE, SQUARE_SIZE
from minesweeper.controls import switch_window, screenshot
from minesweeper.image import crop
from minesweeper.logic import Board
from minesweeper.models import Point


def main():
    switch_window()
    screen = screenshot()
    # switch_window()
    field = crop(screen, START, END)
    board = Board.from_image(field, START, BOARD_SIZE, SQUARE_SIZE)
    board.click(Point(0, 0))
    board.basic_strategy()

    # new_im = Image.new('RGB', field.size)
    #
    # x_offset = 0
    # y_offset = 0
    # for ima in board.squares:
    #     for im in ima:
    #         new_im.paste(im, (x_offset, y_offset))
    #         x_offset += im.size[0]
    #     x_offset = 0
    #     y_offset += im.size[1]

    pass


if __name__ == '__main__':
    main()

