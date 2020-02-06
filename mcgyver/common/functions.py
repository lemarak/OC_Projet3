#! /usr/bin/env python3
# coding: utf-8

"""    project functions    """

from os import path
import pygame as py

from mcgyver.labyrinth import position as pos

# from .. import position as pos
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


def generate_structure(file_path):
    """    generate the labyrinth structure   """

    with open(file_path, 'r') as fil:  # open the file
        structure_grid = []
        pos_y = 0
        for row in fil:     # read each row of the file
            pos_x = 0
            for sprite in row:   # read each value in a row
                if sprite != '\n':
                    position = pos.Position(pos_x, pos_y, sprite)
                    # line_grid.append(sprite)
                    pos_x += 1
                structure_grid.append(position)
            pos_y += 1
    return structure_grid


def display_map(map_laby, structure):
    """    display the labyrinth map   """

    decor = py.transform.scale2x(
        py.image.load(
            picture_file_path(c.IMG_DECOR)
        )).convert()

    for position in structure:
        sprite_position = None
        if position.type_sprite == 'w':
            sprite_position = (c.X_WALL*2, c.Y_WALL*2, 40, 40)
        elif position.type_sprite == '0':
            sprite_position = (c.X_FLOOR*2, c.Y_FLOOR*2, 40, 40)

        if sprite_position:
            map_laby.blit(decor,
                          (position.x_pixel, position.y_pixel),
                          (sprite_position)
                          )

    py.display.flip()
