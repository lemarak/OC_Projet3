#! /usr/bin/env python3
# coding: utf-8

"""    Class Position    """
import copy
import pygame as py

from mcgyver.common import config as c


class Position:
    """ Class Position
        x_sprite
        y_sprite
        type_sprite : "w" for wall, "0" for nothing...
    """

    def __init__(self, x_sprite, y_sprite, type_sprite):
        self.x_sprite = x_sprite
        self.y_sprite = y_sprite
        self.type_sprite = type_sprite

    def __repr__(self):
        string_to_format = "(x_sprite: {}, y_sprite: {}, x_pixel: {}, \
                             x_pixel: {}, type_sprite: {})"

        return string_to_format.format(self.x_sprite,
                                       self.y_sprite,
                                       self.x_pixel,
                                       self.y_pixel,
                                       self.type_sprite,
                                       )

    @property
    def x_pixel(self):
        """ position x in pixel """
        return self.x_sprite * c.SIZE_SPRITE

    @property
    def y_pixel(self):
        """ position x in pixel """
        return self.y_sprite * c.SIZE_SPRITE

    def new_position(self, direction):
        """   return the new position excepted after move   """
        new_pos = copy.copy(self)
        if direction == py.K_RIGHT:
            new_pos.x_sprite += 1
        elif direction == py.K_LEFT:
            new_pos.x_sprite -= 1
        elif direction == py.K_UP:
            new_pos.y_sprite -= 1
        elif direction == py.K_DOWN:
            new_pos.y_sprite += 1
        return new_pos

    def is_valide(self):
        """    determines if position is valid    """
        if self.type_sprite == "w":
            return False
        return True
