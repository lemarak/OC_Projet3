#! /usr/bin/env python3
# coding: utf-8

"""    project functions    """

from os import path
import pygame as py

from mcgyver.labyrinth.mapelement import Hero, Guard
from mcgyver.labyrinth.maplaby import MapLaby
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


def create_avatar(surface_laby, sprite_avatar):
    """    create and display avatar
           sprite_avatar = 'D' for Hero,
                         = 'A' for Guard    """
    position = MapLaby.find_position(sprite_avatar)
    if sprite_avatar == 'D':
        return Hero(surface_laby, position)
    return Guard(surface_laby, position)


def display_end(surface_laby, win, position):
    """   display the end of game,
            choose die or win pucture and display it   """
    end_picture_sprite = py.image.load(
        picture_file_path(c.IMG_END)).convert_alpha()
    if win:
        # You win
        sprite_position = (c.X_WIN, c.Y_WIN, c.SIZE_SPRITE, c.SIZE_SPRITE)
        end_picture_board = py.transform.scale2x(
            py.image.load(
                picture_file_path(c.IMG_WIN))).convert()
    else:
        # You die
        sprite_position = (c.X_DIE, c.Y_DIE, c.SIZE_SPRITE, c.SIZE_SPRITE)
        end_picture_board = py.transform.scale2x(
            py.image.load(
                picture_file_path(c.IMG_DIE))).convert()

    surface_laby.blit(end_picture_sprite,
                      (position.x_pixel, position.y_pixel),
                      (sprite_position)
                      )
    py.display.flip()

    py.time.delay(1000)

    surface_laby.blit(end_picture_board, (75, 75))
    py.display.flip()
