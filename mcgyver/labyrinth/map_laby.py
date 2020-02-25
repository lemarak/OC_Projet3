#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""    Class Map
       STRUCTURE = 2D list of positions    """

import random
import pygame as py

from mcgyver.common import config as c
from mcgyver.common import functions as f
from .position import Position


class MapLaby():
    """    Class Map
           Labyrinth structure    """

    def __init__(self, file_grid, surface_laby):
        self.__map_file = file_grid
        self.__decor = py.transform.scale2x(
            py.image.load(
                f.picture_file_path(c.IMG_DECOR)
            )).convert()
        self.__surface_laby = surface_laby
        self.structure = self.generate_structure()

    @property
    def start(self):
        """   returns the start position   """
        return self.find_position('D')

    @property
    def end(self):
        """   returns the end position   """
        return self.find_position('A')

    def generate_structure(self):
        """    generate the labyrinth structure   """

        with open(self.__map_file, 'r') as fil:  # open the file
            structure_grid = []
            for pos_y, row in enumerate(fil):     # read each row
                structure_row = [Position(pos_x, pos_y, sprite)
                                 for pos_x, sprite in enumerate(row)
                                 if sprite != '\n']
                structure_grid.append(structure_row)
        return structure_grid

    def display_map(self):
        """    display the labyrinth map   """
        # browse the structure
        for row in self.structure:
            for position in row:
                sprite_position = None
                if position.type_sprite == 'w':
                    sprite_position = (c.X_WALL*2, c.Y_WALL*2, 40, 40)
                elif position.type_sprite == '0':
                    sprite_position = (c.X_FLOOR*2, c.Y_FLOOR*2, 40, 40)

                if sprite_position:
                    self.__surface_laby.blit(self.__decor,
                                             (position.x_pixel,
                                              position.y_pixel),
                                             (sprite_position)
                                             )

        py.display.flip()

    def display_element(self, elt):
        """    display object    """
        self.__surface_laby.blit(elt.img_element, (elt.position.x_pixel,
                                                   elt.position.y_pixel))
        py.display.flip()

    def refresh_one_sprite(self, position):
        """    refresh just a sprite instead all the map    """
        sprite_position = (c.X_FLOOR*2, c.Y_FLOOR*2, 40, 40)
        self.__surface_laby.blit(self.__decor,
                                 (position.x_pixel, position.y_pixel),
                                 (sprite_position)
                                 )

    def random_position(self):
        """    returns a random position for the object    """
        # flat the list structure and keep only floor "type_sprite" = 0
        structure_map = [j for sub in self.structure for j in sub]
        structure_floor = [position for position in structure_map
                           if position.type_sprite == "0"]
        position = random.choice(structure_floor)
        return position

    def find_position(self, to_find):
        """    return the position to_find from structure,
               to_find = type_sprite
               unique occurence    """
        structure_map = [j for sub in self.structure for j in sub]
        positions = [position for position in structure_map
                     if position.type_sprite == to_find]
        if len(positions) != 1:
            raise ValueError('incorrect structure !')
        return positions[0]

    def is_valide(self, pos):
        """    check if the new position is valid,
               and return True or False    """
        if pos.x_sprite < 0 or pos.x_sprite >= c.NB_SPRITES \
                or pos.y_sprite < 0 or pos.y_sprite >= c.NB_SPRITES:
            return False
        if self.structure[pos.y_sprite][pos.x_sprite].type_sprite == 'w':
            return False
        return True
