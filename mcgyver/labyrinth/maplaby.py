#! /usr/bin/env python3
# coding: utf-8

"""    Class Map
       STRUCTURE = 2D list of positions    """

import random
import pygame as py

from mcgyver.common import config as c
from mcgyver.common import functions as f
from .position import Position


class MapLaby():
    """    Class Map    """
    STRUCTURE = []

    def __init__(self, file_grid):
        self.__map_file = file_grid
        self.__decor = py.transform.scale2x(
            py.image.load(
                f.picture_file_path(c.IMG_DECOR)
            )).convert()

        self.generate_structure()

    def generate_structure(self):
        """    generate the labyrinth structure   """

        if len(MapLaby.STRUCTURE) == 0:
            with open(self.__map_file, 'r') as fil:  # open the file
                structure_grid = []
                for pos_y, row in enumerate(fil):     # read each row
                    structure_row = []
                    for pos_x, sprite in enumerate(row):  # read each value
                        if sprite != '\n':
                            position = Position(pos_x, pos_y, sprite)
                        structure_row.append(position)
                    structure_grid.append(structure_row)
            MapLaby.STRUCTURE = structure_grid

    def display_map(self, surface_laby):
        """    display the labyrinth map   """

        for row in MapLaby.STRUCTURE:
            for position in row:
                sprite_position = None
                if position.type_sprite == 'w':
                    sprite_position = (c.X_WALL*2, c.Y_WALL*2, 40, 40)
                elif position.type_sprite == '0':
                    sprite_position = (c.X_FLOOR*2, c.Y_FLOOR*2, 40, 40)

                if sprite_position:
                    surface_laby.blit(self.__decor,
                                      (position.x_pixel, position.y_pixel),
                                      (sprite_position)
                                      )

        py.display.flip()

    @classmethod
    def random_position(cls):
        """    returns a random position for the object    """
        # flat the list structure and keep only floor "type_sprite" = 0
        structure_map = [j for sub in cls.STRUCTURE for j in sub]
        structure_floor = [position for position in structure_map
                           if position.type_sprite == "0"]
        position_num = random.randrange(0, len(structure_floor))
        return structure_floor[position_num]

    def refresh_one_sprite(self, surface_laby, position):
        """    refresh just a sprite instead all the map    """
        sprite_position = (c.X_FLOOR*2, c.Y_FLOOR*2, 40, 40)
        surface_laby.blit(self.__decor,
                          (position.x_pixel, position.y_pixel),
                          (sprite_position)
                          )

    @staticmethod
    def find_position(to_find):
        """    return the position to_find from structure,
               to_find = type_sprite    """
        for row in MapLaby.STRUCTURE:
            for position in row:
                if position.type_sprite == to_find:
                    return position
        return None

    @staticmethod
    def is_valide(pos):
        """    check if the new position is valid,
               and return True or False    """
        if pos.x_sprite < 0 or pos.x_sprite >= c.NB_SPRITES \
                or pos.y_sprite < 0 or pos.y_sprite >= c.NB_SPRITES:
            return False
        if MapLaby.STRUCTURE[pos.y_sprite][pos.x_sprite].type_sprite == 'w':
            return False
        return True
