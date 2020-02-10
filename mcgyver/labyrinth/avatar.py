#! /usr/bin/env python3
# coding: utf-8

"""    CLass Hero    """

import pygame as py

from mcgyver.common import functions as f
from mcgyver.common import config as c


class Avatar:

    """   Class parent for avatar (Hero and Guard)   """

    def __init__(self, position, map_laby):
        self.position = position
        self.map_laby = map_laby
        self.img_avatar = None

    def display(self):
        """    display the guard    """
        self.map_laby.blit(self.img_avatar, (self.position.x_pixel,
                                             self.position.y_pixel))
        py.display.flip()


class Guard(Avatar):

    """
    Class to implement the guard
    """

    def __init__(self, position, map_laby):
        Avatar.__init__(self, position, map_laby)
        self.img_avatar = py.image.load(
            f.picture_file_path(c.IMG_GUARD)).convert()


class Hero(Avatar):

    """
    class to implement the Hero (MacGyver)
    """

    def __init__(self, position, map_laby):
        Avatar.__init__(self, position, map_laby)
        self.objects = []
        self.img_avatar = py.image.load(
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
