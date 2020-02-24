#! /usr/bin/env python3
# coding: utf-8

"""    class to implements objects (avatar and objects to find)    """

import pygame as py

from mcgyver.common import config as c
from mcgyver.common import functions as f


class MapElement:
    """    parent Class to implement objects    """

    def __init__(self, map_laby):
        """    constructor    """
        self.map_laby = map_laby
        self.position = None
        self.img_element = None


class Hero(MapElement):

    """
    class to implement the Hero (MacGyver)
    """

    def __init__(self, map_laby):
        MapElement.__init__(self, map_laby)
        self.position = map_laby.start
        self.objects = []
        self.img_element = py.image.load(
            f.picture_file_path(c.IMG_HERO)).convert()
        map_laby.display_element(self)

    def check_object(self, objects_array):
        """    check if Hero position on object    """
        for obj in objects_array:
            if self.position == obj.position and obj not in self.objects:
                self.objects.append(obj)
                return True
        return False

    @property
    def nb_objects(self):
        """    Number of items held by McGyver    """
        return len(self.objects)


class Guard(MapElement):

    """
    Class to implement the guard
    """

    def __init__(self, map_laby):
        MapElement.__init__(self, map_laby)
        self.position = map_laby.end
        self.img_element = py.image.load(
            f.picture_file_path(c.IMG_GUARD)).convert()
        map_laby.display_element(self)


class Needle(MapElement):
    """    Child Class needle from MapElement    """

    def __init__(self, map_laby):
        MapElement.__init__(self, map_laby)
        self.position = map_laby.random_position()
        self.img_element = py.image.load(
            f.picture_file_path(c.IMG_NEEDLE)).convert()
        map_laby.display_element(self)


class Tube(MapElement):
    """    Child Class for tube    """

    def __init__(self, map_laby):
        MapElement.__init__(self, map_laby)
        self.position = map_laby.random_position()
        self.img_element = py.image.load(
            f.picture_file_path(c.IMG_TUBE)).convert_alpha()
        map_laby.display_element(self)


class Ether(MapElement):
    """    Child Class for ether    """

    def __init__(self, map_laby):
        MapElement.__init__(self, map_laby)
        self.position = map_laby.random_position()
        self.img_element = py.image.load(
            f.picture_file_path(c.IMG_ETHER)).convert_alpha()
        map_laby.display_element(self)
