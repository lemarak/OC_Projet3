#! /usr/bin/env python3
# coding: utf-8

"""    project functions    """

from os import path
import pygame as py

from ..common import config as c


def picture_file_path(img_file):
    """    returns the full path of the image file    """
    path_file = path.dirname(path.dirname(__file__))
    return path.join(path_file, c.PATH_PICTURES, img_file)


def grid_file_path(file):
    """    Return the path of file = grid.txt,
        structure of the labyrinth    """

    path_file = path.dirname(path.dirname(__file__))
    return path.join(path_file, c.PATH_GRID, file)


def display_title(nb_objects, message=""):
    """    display title of map    """

    if message == "end":
        if nb_objects == 3:
            message = "***  You win !!!  ***"
        else:
            message = "***  You die !!!  ***"
    title_map = "{} {} {}/3 objects  {}".format(c.TXT_TITLE, " "*8,
                                                nb_objects, message)
    py.display.set_caption(title_map)
    py.display.flip()


def display_end(surface_laby, win, position):
    """   display the end of game,
            choose die or win pucture and display it   """
    end_picture = py.image.load(
        picture_file_path(c.IMG_END)).convert_alpha()
    if win:
        sprite_position = (c.X_WIN, c.Y_WIN, c.SIZE_SPRITE, c.SIZE_SPRITE)
    else:
        sprite_position = (c.X_DIE, c.Y_DIE, c.SIZE_SPRITE, c.SIZE_SPRITE)

    surface_laby.blit(end_picture,
                      (position.x_pixel, position.y_pixel),
                      (sprite_position)
                      )
    py.display.flip()
