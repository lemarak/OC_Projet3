#! /usr/bin/env python3
# coding: utf-8

"""    class to implements objects    """

import pygame as py

from mcgyver.common import config as c
from mcgyver.common import functions as f
from mcgyver.labyrinth import position as pos


class LabyObject:
    """    parent Class to implement objects    """

    def __init__(self, position):
        """    constructor    """
        self.position = position


class Needle(LabyObject):
    """    Child Class for needle    """
    def __init__(self):
        super().__init__(self)
        self.img_hero = py.image.load(
            f.picture_file_path(c.IMG_HERO)).convert()


class Tube(LabyObject):
    """    Child Class for tube    """
    def __init__(self):
        super().__init__(self)
        self.img_hero = py.image.load(
            f.picture_file_path(c.IMG_HERO)).convert()


class Ether(LabyObject):
    """    Child Class for ether    """
    def __init__(self):
        super().__init__(self)
        self.img_hero = py.image.load(
            f.picture_file_path(c.IMG_HERO)).convert()
