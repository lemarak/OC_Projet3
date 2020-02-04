#! /usr/bin/env python3
# coding: utf-8

"""    project functions    """

from os import path
import pygame as py

from . import constants as c


def picture_file_path(img_file):
    """    returns the full path of the image file    """
    path_file = path.dirname(path.dirname(__file__))
    print("path_file :", path_file)
    print("path.join :", path.join(path_file, c.PATH_PICTURES, img_file))
    return path.join(path_file, c.PATH_PICTURES, img_file)


def grid_file_path(file):
    """Return the path of grid.txt,
        structure of the labyrinth"""

    path_file = path.dirname(__file__)
    return path.join(path_file, c.PATH_GRID, file)


def generate_structure(file_path):
    """    generate the labyrinth structure   """

    with open(file_path, 'r') as fil:  # open the file
        structure_grid = []
        for row in fil:     # read each row of the file
            line_grid = []
            for sprite in row:   # read each value in a row
                if sprite != '\n':
                    line_grid.append(sprite)
            structure_grid.append(line_grid)
    return structure_grid


def display_labyrinth(surface_laby, structure):
    """    display the labyrinth    """

    wall = py.image.load(picture_file_path(c.IMG_WALL)).convert()

    num_row = 0
    for row in structure:
        num_cell = 0
        for sprite in row:
            pos_x = num_cell * c.SIZE_SPRITE
            pos_y = num_row * c.SIZE_SPRITE
            if sprite == 'm':
                surface_laby.blit(wall, (pos_x, pos_y), (40, 0, 20, 20))
            num_cell += 1
        num_row += 1

    py.display.flip()

    progress = 1
    while progress:
        progress = int(input())
