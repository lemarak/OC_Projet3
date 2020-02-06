#! /usr/bin/env python3
# coding: utf-8

"""    Class Guard    """
import pygame as py

from mcgyver.common import functions as f
from mcgyver.common import config as c


class Guard:

    """
    Class to implement the guard
    """

    def __init__(self, position, map_laby):
        self.position = position
        self.map_laby = map_laby

    def display(self):
        """    display the guard    """
        img_hero = py.image.load(f.picture_file_path(c.IMG_GUARD)).convert()
        self.map_laby.blit(img_hero, (self.position.x_pixel,
                                      self.position.y_pixel))
        py.display.flip()
