#! /usr/bin/env python3
# coding: utf-8

"""    class to implements objects (avatar and objects to find)    """

import pygame as py

from mcgyver.common import config as c
from mcgyver.common import functions as f

# from mcgyver.labyrinth import position as pos


class MapElement:
    """    parent Class to implement objects    """

    def __init__(self, surface_laby, position):
        """    constructor    """
        self.surface_laby = surface_laby
        self.position = position
        self.img_element = None

    def display(self):
        """    display object    """
        self.surface_laby.blit(self.img_element, (self.position.x_pixel,
                                                  self.position.y_pixel))
        py.display.flip()


class Guard(MapElement):

    """
    Class to implement the guard
    """

    def __init__(self, surface_laby, position):
        MapElement.__init__(self, surface_laby, position)
        self.img_element = py.image.load(
            f.picture_file_path(c.IMG_GUARD)).convert()
        self.display()


class Hero(MapElement):

    """
    class to implement the Hero (MacGyver)
    """

    def __init__(self, surface_laby, position):
        MapElement.__init__(self, surface_laby, position)
        self.objects = []
        self.img_element = py.image.load(
            f.picture_file_path(c.IMG_HERO)).convert()
        self.display()

    def check_object(self, objects_array):
        """    check if Hero on object    """
        for obj in objects_array:
            if self.position == obj.position and obj not in self.objects:
                self.objects.append(obj)
                return True
        return False

    @property
    def nb_objects(self):
        """    Number of items held by McGyver    """
        return len(self.objects)


class Needle(MapElement):
    """    Child Class needle from MapElement    """

    def __init__(self, surface_laby, position):
        MapElement.__init__(self, surface_laby, position)
        self.img_element = py.image.load(
            f.picture_file_path(c.IMG_NEEDLE)).convert()
        self.display()


class Tube(MapElement):
    """    Child Class for tube    """

    def __init__(self, surface_laby, position):
        MapElement.__init__(self, surface_laby, position)
        self.img_element = py.image.load(
            f.picture_file_path(c.IMG_TUBE)).convert_alpha()
        self.display()


class Ether(MapElement):
    """    Child Class for ether    """

    def __init__(self, surface_laby, position):
        MapElement.__init__(self, surface_laby, position)
        self.img_element = py.image.load(
            f.picture_file_path(c.IMG_ETHER)).convert_alpha()
        self.display()
