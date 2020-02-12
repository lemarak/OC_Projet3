#! /usr/bin/env python3
# coding: utf-8

"""    class to implements objects    """

import pygame as py

from mcgyver.common import config as c
from mcgyver.common import functions as f
# from mcgyver.labyrinth import position as pos


class MapElement:
    """    parent Class to implement objects    """

    def __init__(self, position, map_laby):
        """    constructor    """
        self.position = position
        self.map_laby = map_laby
        self.img_element = None

    def display(self):
        """    display object    """
        self.map_laby.blit(self.img_element, (self.position.x_pixel,
                                              self.position.y_pixel))
        py.display.flip()


class Guard(MapElement):

    """
    Class to implement the guard
    """

    def __init__(self, position, map_laby):
        MapElement.__init__(self, position, map_laby)
        self.img_element = py.image.load(
            f.picture_file_path(c.IMG_GUARD)).convert()


class Hero(MapElement):

    """
    class to implement the Hero (MacGyver)
    """

    def __init__(self, position, map_laby):
        MapElement.__init__(self, position, map_laby)
        self.objects = []
        self.img_element = py.image.load(
            f.picture_file_path(c.IMG_HERO)).convert()

    def check_object(self, objects_array):
        """    check if Hero on object    """
        for obj in objects_array:
            if self.position == obj.position and obj not in self.objects:
                self.objects.append(obj)
                print("McGyver objects :", self.nb_objects)

    @property
    def nb_objects(self):
        """    Number of items held by McGyver    """
        return len(self.objects)


class Needle(MapElement):
    """    Child Class needle from MapElement    """

    def __init__(self, position, map_laby):
        MapElement.__init__(self, position, map_laby)
        self.img_element = py.image.load(
            f.picture_file_path(c.IMG_NEEDLE)).convert()


class Tube(MapElement):
    """    Child Class for tube    """

    def __init__(self, position, map_laby):
        MapElement.__init__(self, position, map_laby)
        self.img_element = py.image.load(
            f.picture_file_path(c.IMG_TUBE)).convert_alpha()


class Ether(MapElement):
    """    Child Class for ether    """

    def __init__(self, position, map_laby):
        MapElement.__init__(self, position, map_laby)
        self.img_element = py.image.load(
            f.picture_file_path(c.IMG_ETHER)).convert_alpha()
