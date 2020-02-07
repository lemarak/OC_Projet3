#! /usr/bin/env python3
# coding: utf-8

"""    Main program    """

import pygame as py

from mcgyver.common import config as c
from mcgyver.common import functions as f
from mcgyver.labyrinth import hero
from mcgyver.labyrinth import guard
from mcgyver.labyrinth import maplaby
from mcgyver.labyrinth import mapobject


def main():
    """    main program    """

    py.init()  # pylint: disable=maybe-no-member

    # labyrinth initialisation, surface_laby type(surface)
    surface_laby = py.display.set_mode((c.WINDOW_SIZE,
                                        c.WINDOW_SIZE))
    py.display.set_caption(c.TXT_TITLE)
    icon = py.image.load(f.picture_file_path(c.IMG_ICON)).convert()
    py.display.set_icon(icon)

    # generate the structure of the labyrinth from a text file
    path_file_structure = f.grid_file_path("grid.txt")
    map_laby = maplaby.MapLaby(path_file_structure)
    map_laby.generate_structure()

    # display map structure
    map_laby.display_map(surface_laby)

    # initialize, position and display the Hero
    position_hero = map_laby.find_position('D')
    mcgyver = hero.Hero(position_hero, surface_laby)
    mcgyver.display()

    # initialize, position and display the Guard
    position_guard = map_laby.find_position('A')
    bad_guy = guard.Guard(position_guard, surface_laby)
    bad_guy.display()

    # initialize, position and display the needle
    needle = mapobject.Needle(map_laby)
    needle.display()

    # pymap event management
    progress = True
    while progress:
        for event in py.event.get():
            if event.type == py.QUIT:
                progress = False
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    progress = False
                elif event.key in [py.K_RIGHT, py.K_LEFT, py.K_UP, py.K_DOWN]:
                    new_x, new_y = mcgyver.position.new_position(event.key)
                    if map_laby.is_valide(new_x, new_y):
                        new_position = map_laby.structure[new_y][new_x]
                        map_laby.refresh_one_sprite(surface_laby,
                                                    mcgyver.position)
                        mcgyver.position = new_position
                        mcgyver.display()

    py.quit()  # pylint: disable=maybe-no-member


if __name__ == "__main__":
    main()
