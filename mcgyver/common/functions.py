#! /usr/bin/env python3
# coding: utf-8

"""    project functions    """

from os import path

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
