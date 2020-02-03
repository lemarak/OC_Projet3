#! /usr/bin/env python3
# coding: utf-8

"""    Main program    """


import pygame as py

import labyrinthe.grid as grid
import constants


def main():
    """    main program    """

    # py.init()

    window = py.display.set_mode((constants.WINDOW_SIZE,
                                  constants.WINDOW_SIZE))
    py.display.set_caption(constants.TXT_TITLE)

    grille = grid.Grid('grid.txt')
    grille.generate()
    print(grille.structure)
    grille.display(window)


if __name__ == "__main__":
    main()
