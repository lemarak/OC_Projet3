#! /usr/bin/env python3
# coding: utf-8

"""    Main program    """

import sys
import pygame as py
from pygame import locals as pyloc

from mcgyver.common import config as c
from mcgyver.common import functions as f


sys.path.append("..")
sys.path.append(".")


def main():
    """    main program    """

    py.init()  # pylint: disable=maybe-no-member

    surface = py.display.set_mode((c.WINDOW_SIZE,
                                   c.WINDOW_SIZE))
    py.display.set_caption(c.TXT_TITLE)

    # generate the structure of the labyrinth from a text file
    path_file_structure = f.grid_file_path("grid.txt")
    structure = f.generate_structure(path_file_structure)
    print([pos for pos in structure])

    f.display_labyrinth(surface, structure)

    progress = 1
    while progress:
        for event in py.event.get():
            if event.type == pyloc.QUIT:
                py.quit()
                progress = 0

    py.quit()  # pylint: disable=maybe-no-member


if __name__ == "__main__":
    main()
