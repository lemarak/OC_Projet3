#! /usr/bin/env python3
# coding: utf-8

"""    CLass Hero    """

import pygame as py

from mcgyver.common import functions as f
from mcgyver.common import config as c


class Hero:

    """
    class to implement the Hero (MacGyver)
    """

    def __init__(self, position, map_laby):
        self.position = position
        self.map_laby = map_laby

    def display(self):
        """    display the hero    """
        img_hero = py.image.load(f.picture_file_path(c.IMG_HERO)).convert()
        self.map_laby.blit(img_hero, (self.position.x_pixel,
                                      self.position.y_pixel))
        py.display.flip()
