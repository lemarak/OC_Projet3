#! /usr/bin/env python3
# coding: utf-8

"""    Main program    """

import pygame as py

from mcgyver.common import config as c
from mcgyver.common import functions as f
from mcgyver.labyrinth import hero
from mcgyver.labyrinth import guard


def main():
    """    main program    """

    py.init()  # pylint: disable=maybe-no-member

    # labyrinth initialisation
    map_laby = py.display.set_mode((c.WINDOW_SIZE,
                                    c.WINDOW_SIZE))
    py.display.set_caption(c.TXT_TITLE)
    icon = py.image.load(f.picture_file_path(c.IMG_ICON)).convert()
    py.display.set_icon(icon)

    # generate the structure of the labyrinth from a text file
    path_file_structure = f.grid_file_path("grid.txt")
    structure = f.generate_structure(path_file_structure)

    # display map structure
    f.display_map(map_laby, structure)

    # initialize, position and display the Hero
    index_position_hero = [pos.type_sprite for pos in structure].index('H')
    mcgyver = hero.Hero(structure[index_position_hero], map_laby)
    mcgyver.display()

    # initialize, position and display the Guard
    index_position_guard = [pos.type_sprite for pos in structure].index('G')
    bad_guy = guard.Guard(structure[index_position_guard], map_laby)
    bad_guy.display()

    progress = True
    while progress:
        for event in py.event.get():
            if event.type == py.QUIT:
                progress = False
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    progress = False

    py.quit()  # pylint: disable=maybe-no-member


if __name__ == "__main__":
    main()
