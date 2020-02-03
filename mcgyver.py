#! /usr/bin/env python3
# coding: utf-8

"""    Main program    """


import pygame as py

import labyrinthe.grid as grid
import constants as c


def main():
    """    main program    """

    # py.init()

    window = py.display.set_mode((c.WINDOW_SIZE,
                                  c.WINDOW_SIZE))
    py.display.set_caption(c.TXT_TITLE)

    grille = grid.Grid('grid.txt')
    grille.generate()
    print(grille.structure)
    grille.display(window)


if __name__ == "__main__":
    main()
