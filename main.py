#! /usr/bin/env python3
# coding: utf-8

"""    Main program    """

import pygame as py

from mcgyver.common import config as c
from mcgyver.common import functions as f
from mcgyver.labyrinth import maplaby
from mcgyver.labyrinth import mapelement


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
    map_laby = maplaby.MapLaby(path_file_structure)
    map_laby.generate_structure()

    # display map structure
    map_laby.display_map(surface_laby)

    # initialize, position and display the Avatar and objects
    # todo: refactoring
    position = map_laby.find_position('D')
    mcgyver = mapelement.Hero(surface_laby, position)
    position = map_laby.find_position('A')
    bad_guy = mapelement.Guard(surface_laby, position)
    position = map_laby.random_position()
    needle = mapelement.Needle(surface_laby, position)
    position = map_laby.random_position()
    tube = mapelement.Tube(surface_laby, position)
    position = map_laby.random_position()
    ether = mapelement.Ether(surface_laby, position)

    objects_array = [needle, tube, ether]
    f.display_title(mcgyver.nb_objects)

    # pymap event management
    progress = True
    end_of_game = False

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
                    new_x, new_y = mcgyver.position.new_position(event.key)
                    if map_laby.is_valide(new_x, new_y):
                        new_position = map_laby.structure[new_y][new_x]
                        map_laby.refresh_one_sprite(surface_laby,
                                                    mcgyver.position)
                        mcgyver.position = new_position
                        mcgyver.display()
                        if mcgyver.check_object(objects_array):
                            f.display_title(mcgyver.nb_objects)
                        if mcgyver.position == bad_guy.position:
                            f.display_title(mcgyver.nb_objects, "end")
                            win = (mcgyver.nb_objects == 3)
                            f.display_end(surface_laby, win, mcgyver.position)
                            end_of_game = True

    py.quit()  # pylint: disable=maybe-no-member


if __name__ == "__main__":
    main()
