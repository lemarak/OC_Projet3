#! /usr/bin/env python3
# coding: utf-8

"""    Main program    """

import pygame as py

import labyrinth.constants as c
import labyrinth.functions as f


def main():
    """    main program    """

    py.init()  # pylint: disable=maybe-no-member

    surface = py.display.set_mode((c.WINDOW_SIZE,
                                   c.WINDOW_SIZE))
    py.display.set_caption(c.TXT_TITLE)

    # generate the structure of the labyrinth from a text file
    path_file_structure = f.grid_file_path("grid.txt")
    structure = f.generate_structure(path_file_structure)

    print(structure)
    f.display_labyrinth(surface, structure)

    py.quit()  # pylint: disable=maybe-no-member


if __name__ == "__main__":
    main()
