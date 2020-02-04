#! /usr/bin/env python3
# coding: utf-8

"""    Class Position    """

from .. import constants as c


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
        string_to_format = "(x: {}, y: {}, x_pixel: {}, x_pixel: {}, type: {})"
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
