#! /usr/bin/env python3
# coding: utf-8

"""    Main program    """

import pygame as py

from mcgyver.common import config as c
from mcgyver.common import functions as f
from mcgyver.labyrinth.maplaby import MapLaby
from mcgyver.labyrinth.mapelement import Hero, Guard
from mcgyver.labyrinth.mapelement import Needle, Tube, Ether


def main():
    """    main program    """

    py.init()  # pylint: disable=maybe-no-member

    # labyrinth initialisation, surface_laby type(surface)
    surface_laby = py.display.set_mode((c.WINDOW_SIZE,
                                        c.WINDOW_SIZE))

    icon = py.image.load(f.picture_file_path(c.IMG_ICON))
    py.display.set_icon(icon)

    # generate the structure of the labyrinth from a text file
    path_file_structure = f.grid_file_path("grid.txt")
    map_laby = MapLaby(path_file_structure, surface_laby)

    # display map structure
    map_laby.display_map()

    # initialize, position and display the Avatar and objects
    mcgyver = Hero(map_laby)
    Guard(map_laby)
    needle = Needle(map_laby)
    tube = Tube(map_laby)
    ether = Ether(map_laby)

    objects_array = [needle, tube, ether]
    f.display_title(mcgyver.nb_objects)

    # pymap event management
    progress = True     # False when the game is stopped (escape or alt-f4)
    end_of_game = False  # True when the hero reaches his goal, he stops moving

    while progress:
        for event in py.event.get():
            if event.type == py.QUIT:  # pylint: disable=maybe-no-member
                progress = False

            if event.type == py.KEYDOWN:  # pylint: disable=maybe-no-member

                if event.key == py.K_ESCAPE:  # pylint: disable=maybe-no-member
                    progress = False
                elif not end_of_game and event.key in \
                        [py.K_RIGHT,    # pylint: disable=maybe-no-member
                         py.K_LEFT,  # pylint: disable=maybe-no-member
                         py.K_UP,  # pylint: disable=maybe-no-member
                         py.K_DOWN]:  # pylint: disable=maybe-no-member

                    new_position = mcgyver.position.new_position(event.key)

                    # check if the position is valid
                    if map_laby.is_valide(new_position):
                        map_laby.refresh_one_sprite(mcgyver.position)
                        mcgyver.position = new_position
                        map_laby.display_element(mcgyver)

                        # test object
                        if mcgyver.check_object(objects_array):
                            f.display_title(mcgyver.nb_objects)

                        # end of game
                        if mcgyver.position == map_laby.end:
                            f.display_title(mcgyver.nb_objects, "end")
                            win = (mcgyver.nb_objects == 3)
                            f.display_end(surface_laby, win, mcgyver.position)
                            end_of_game = True

    py.quit()  # pylint: disable=maybe-no-member


if __name__ == "__main__":
    main()
