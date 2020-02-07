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
        self.nb_objets = 0
        self.img_hero = py.image.load(
            f.picture_file_path(c.IMG_HERO)).convert()

    def display(self):
        """    display the hero    """
        self.map_laby.blit(self.img_hero, (self.position.x_pixel,
                                           self.position.y_pixel))
        py.display.flip()

    def move(self, direction):
        """    move the Hero    """
        new_pos = self.position.new_position(direction)
        if new_pos.is_valide():
            self.position = new_pos
            self.display()
