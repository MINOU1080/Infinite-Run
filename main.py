import pygame as py

from board.boardPygame import BoardPygame


def main():
    py.init()
    py.display.set_caption('Infinite Run')
    screen = py.display.set_mode((1080, 720))
    game = BoardPygame(screen)
    game.run()


if __name__ == '__main__':
    main()
