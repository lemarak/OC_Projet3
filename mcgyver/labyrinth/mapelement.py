#! /usr/bin/env python3
# coding: utf-8

"""    class to implements objects    """

import random
import pygame as py

from mcgyver.common import config as c
from mcgyver.common import functions as f

# from mcgyver.labyrinth import position as pos


class MapElement:
    """    parent Class to implement objects    """

    def __init__(self, surface_laby, structure_map):
        """    constructor    """
        self.surface_laby = surface_laby
        self.structure_map = structure_map
        self.position = None
        self.img_element = None

    def display(self):
        """    display object    """
        self.surface_laby.blit(self.img_element, (self.position.x_pixel,
                                                  self.position.y_pixel))
        py.display.flip()

    def random_position(self):
        """    returns a random position for the object    """
        # flat the list structure and keep only floor "type_sprite" = 0
        structure_map = [j for sub in self.structure_map for j in sub]
        structure_floor = [position for position in structure_map
                           if position.type_sprite == "0"]
        position_num = random.randrange(0, len(structure_floor))
        return structure_floor[position_num]

    def find_position(self, to_find):
        """    return the position to_find from structure,
               to_find = type_sprite    """
        for row in self.structure_map:
            for position in row:
                if position.type_sprite == to_find:
                    return position
        return None


class Guard(MapElement):

    """
    Class to implement the guard
    """

    def __init__(self, surface_laby, structure_map):
        MapElement.__init__(self, surface_laby, structure_map)
        self.img_element = py.image.load(
            f.picture_file_path(c.IMG_GUARD)).convert()
        self.position = self.find_position('A')
        self.display()


class Hero(MapElement):

    """
    class to implement the Hero (MacGyver)
    """

    def __init__(self, surface_laby, structure_map):
        MapElement.__init__(self, surface_laby, structure_map)
        self.objects = []
        self.img_element = py.image.load(
            f.picture_file_path(c.IMG_HERO)).convert()
        self.position = self.find_position('D')
        self.display()

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

    def __init__(self, surface_laby, structure_map):
        MapElement.__init__(self, surface_laby, structure_map)
        self.position = self.random_position()
        self.img_element = py.image.load(
            f.picture_file_path(c.IMG_NEEDLE)).convert()
        self.display()


class Tube(MapElement):
    """    Child Class for tube    """

    def __init__(self, surface_laby, structure_map):
        MapElement.__init__(self, surface_laby, structure_map)
        self.position = self.random_position()
        self.img_element = py.image.load(
            f.picture_file_path(c.IMG_TUBE)).convert_alpha()
        self.display()


class Ether(MapElement):
    """    Child Class for ether    """

    def __init__(self, surface_laby, structure_map):
        MapElement.__init__(self, surface_laby, structure_map)
        self.position = self.random_position()
        self.img_element = py.image.load(
            f.picture_file_path(c.IMG_ETHER)).convert_alpha()
        self.display()
