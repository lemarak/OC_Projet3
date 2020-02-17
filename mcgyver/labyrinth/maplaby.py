#! /usr/bin/env python3
# coding: utf-8

"""    Class Map
       STRUCTURE = 2D list of positions    """

import random
import pygame as py

from mcgyver.common import config as c
from mcgyver.common import functions as f
from mcgyver.labyrinth import position as pos


class MapLaby():
    """    Class Map    """
    STRUCTURE = []
    DECOR = None
    MAP_FILE = ""

    def __init__(self, file_grid):
        MapLaby.MAP_FILE = file_grid
        MapLaby.DECOR = py.transform.scale2x(
            py.image.load(
                f.picture_file_path(c.IMG_DECOR)
            )).convert()

    @classmethod
    def generate_structure(cls):
        """    generate the labyrinth structure   """

        if len(cls.STRUCTURE) == 0:
            with open(cls.MAP_FILE, 'r') as fil:  # open the file
                structure_grid = []
                pos_y = 0
                for row in fil:     # read each row of the file
                    structure_row = []
                    pos_x = 0
                    for sprite in row:   # read each value in a row
                        if sprite != '\n':
                            position = pos.Position(pos_x, pos_y, sprite)
                            pos_x += 1
                        structure_row.append(position)
                    structure_grid.append(structure_row)
                    pos_y += 1
            cls.STRUCTURE = structure_grid

    @classmethod
    def display_map(cls, surface_laby):
        """    display the labyrinth map   """

        for row in cls.STRUCTURE:
            for position in row:
                sprite_position = None
                if position.type_sprite == 'w':
                    sprite_position = (c.X_WALL*2, c.Y_WALL*2, 40, 40)
                elif position.type_sprite == '0':
                    sprite_position = (c.X_FLOOR*2, c.Y_FLOOR*2, 40, 40)

                if sprite_position:
                    surface_laby.blit(cls.DECOR,
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

    @classmethod
    def refresh_one_sprite(cls, surface_laby, position):
        """    refresh just a sprite instead all the map    """
        sprite_position = (c.X_FLOOR*2, c.Y_FLOOR*2, 40, 40)
        surface_laby.blit(cls.DECOR,
                          (position.x_pixel, position.y_pixel),
                          (sprite_position)
                          )

    @classmethod
    def find_position(cls, to_find):
        """    return the position to_find from structure,
               to_find = type_sprite    """
        print("structure :", cls.STRUCTURE)
        for row in cls.STRUCTURE:
            for position in row:
                if position.type_sprite == to_find:
                    return position
        return None

    @classmethod
    def is_valide(cls, move_x, move_y):
        """    check if the new position is valid,
               and return True or False    """
        if move_x < 0 or move_x >= c.NB_SPRITES \
                or move_y < 0 or move_y >= c.NB_SPRITES:
            return False
        if cls.STRUCTURE[move_y][move_x].type_sprite == 'w':
            return False
        return True
