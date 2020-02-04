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
    print("path_file :", path_file)
    print("path.join :", path.join(path_file, c.PATH_PICTURES, img_file))
    return path.join(path_file, c.PATH_PICTURES, img_file)


def grid_file_path(file):
    """Return the path of file = grid.txt,
        structure of the labyrinth"""

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


def display_labyrinth(surface_laby, structure):
    """    display the labyrinth    """

    decor = py.image.load(picture_file_path(c.IMG_WALL)).convert()

    for position in structure:
        if position.type_sprite == 'w':
            surface_laby.blit(decor,
                              (position.x_pixel, position.y_pixel),
                              (40, 0, 20, 20)
                              )

    py.display.flip()
