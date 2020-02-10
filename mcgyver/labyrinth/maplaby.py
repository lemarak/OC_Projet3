#! /usr/bin/env python3
# coding: utf-8

"""    Class Map    """

import random
import pygame as py

from mcgyver.common import config as c
from mcgyver.common import functions as f
from mcgyver.labyrinth import position as pos


class MapLaby():
    """    Class Map    """

    def __init__(self, file_grid):
        self.map_file = file_grid
        self.structure = []
        self.decor = py.transform.scale2x(
            py.image.load(
                f.picture_file_path(c.IMG_DECOR)
            )).convert()

    # generate the structure for a level

    def generate_structure(self):
        """    generate the labyrinth structure   """

        with open(self.map_file, 'r') as fil:  # open the file
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
        self.structure = structure_grid

    def display_map(self, surface_laby):
        """    display the labyrinth map   """

        for row in self.structure:
            for position in row:
                sprite_position = None
                if position.type_sprite == 'w':
                    sprite_position = (c.X_WALL*2, c.Y_WALL*2, 40, 40)
                elif position.type_sprite == '0':
                    sprite_position = (c.X_FLOOR*2, c.Y_FLOOR*2, 40, 40)

                if sprite_position:
                    surface_laby.blit(self.decor,
                                      (position.x_pixel, position.y_pixel),
                                      (sprite_position)
                                      )

        py.display.flip()

    def refresh_one_sprite(self, surface_laby, position):
        """    refresh just a sprite instead all the map    """
        sprite_position = (c.X_FLOOR*2, c.Y_FLOOR*2, 40, 40)
        surface_laby.blit(self.decor,
                          (position.x_pixel, position.y_pixel),
                          (sprite_position)
                          )

    def find_position(self, to_find):
        """    return the position to_find from structure,
               to_find = type_sprite    """
        for row in self.structure:
            for position in row:
                if position.type_sprite == to_find:
                    return position
        return None

    def is_valide(self, move_x, move_y):
        """    docstring to complete    """
        if move_x < 0 or move_x >= c.NB_SPRITES \
                or move_y < 0 or move_y >= c.NB_SPRITES:
            return False
        if self.structure[move_y][move_x].type_sprite == 'w':
            return False
        return True

    def random_position(self):
        """    returns a random position for the object    """

        structure_map = [j for sub in self.structure for j in sub]
        structure_floor = [position for position in structure_map
                           if position.type_sprite == "0"]
        position_num = random.randrange(0, len(structure_floor))
        return structure_floor[position_num]
