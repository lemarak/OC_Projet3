#! /usr/bin/env python3
# coding: utf-8

"""    class to implements objects    """

import random
import pygame as py

from mcgyver.common import config as c
from mcgyver.common import functions as f
from mcgyver.labyrinth import position as pos


class LabyObject:
    """    parent Class to implement objects    """

    def __init__(self, map_laby):
        """    constructor    """
        self.map_laby = map_laby
        self.position = self.random_position()
        self.img_object = None

    def random_position(self):
        """    returns a random position for the object    """

        structure_rows = [rows for rows in self.map_laby.structure]
        structure_split = [positions for positions in structure_rows
                           if positions.type_sprite == "0"]
        print(structure_split)
        position_num = random.randrange(0, len(structure_split))
        return structure_split[position_num]

    def display(self):
        """    display object    """
        self.map_laby.blit(self.img_object, (self.position.x_pixel,
                                             self.position.y_pixel))
        py.display.flip()


class Needle(LabyObject):
    """    Child Class for needle    """

    def __init__(self, map_laby):
        super().__init__(self)
        self.img_object = py.image.load(
            f.picture_file_path(c.IMG_NEEDLE)).convert_alpha()


class Tube(LabyObject):
    """    Child Class for tube    """

    def __init__(self, map_laby):
        super().__init__(self)
        self.img_object = py.image.load(
            f.picture_file_path(c.IMG_TUBE)).convert_alpha()


class Ether(LabyObject):
    """    Child Class for ether    """

    def __init__(self, map_laby):
        super().__init__(self)
        self.img_object = py.image.load(
            f.picture_file_path(c.IMG_ETHER)).convert_alpha()
