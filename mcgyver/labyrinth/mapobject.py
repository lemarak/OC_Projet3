#! /usr/bin/env python3
# coding: utf-8

"""    class to implements objects    """

import pygame as py

from mcgyver.common import config as c
from mcgyver.common import functions as f
# from mcgyver.labyrinth import position as pos


class LabyObject:
    """    parent Class to implement objects    """

    def __init__(self, position, map_laby):
        """    constructor    """
        self.position = position
        self.map_laby = map_laby
        self.img_object = None

    def display(self):
        """    display object    """
        self.map_laby.blit(self.img_object, (self.position.x_pixel,
                                             self.position.y_pixel))
        py.display.flip()


class Needle(LabyObject):
    """    Child Class needle from LabyObject    """

    def __init__(self, position, map_laby):
        LabyObject.__init__(self, position, map_laby)
        self.img_object = py.image.load(
            f.picture_file_path(c.IMG_NEEDLE)).convert()


class Tube(LabyObject):
    """    Child Class for tube    """

    def __init__(self, position, map_laby):
        LabyObject.__init__(self, position, map_laby)
        self.img_object = py.image.load(
            f.picture_file_path(c.IMG_TUBE)).convert_alpha()


class Ether(LabyObject):
    """    Child Class for ether    """

    def __init__(self, position, map_laby):
        LabyObject.__init__(self, position, map_laby)
        self.img_object = py.image.load(
            f.picture_file_path(c.IMG_ETHER)).convert_alpha()
