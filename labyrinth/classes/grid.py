#! /usr/bin/env python3
# coding: utf-8

"""    Class Grid for create and display labyrinth    """

from os import path
import pygame as py
import pygame.locals

from .. import constants as c
from .. import functions as f


class Grid():
    """    generate and display the labyrinth    """

    def __init__(self, file):
        self.file = file
        self.structure = 0

    def generate(self):
        """    generate the labyrinth structure   """

        with open(self.grid_file_path, 'r') as fil:  # open the file
            structure_grid = []
            for row in fil:     # read each row of the file
                line_grid = []
                for sprite in row:   # read each value in a row
                    if sprite != '\n':
                        line_grid.append(sprite)
                structure_grid.append(line_grid)
        self.structure = structure_grid

    def display(self, surface_laby):
        """    display the labyrinth    """

        print("Grid :", path.dirname(path.dirname(__file__)))
        wall = py.image.load(f.picture_file_path(c.IMG_WALL)).convert()

        num_row = 0
        for row in self.structure:
            num_cell = 0
            for sprite in row:
                pos_x = num_cell * c.SIZE_SPRITE
                pos_y = num_row * c.SIZE_SPRITE
                if sprite == 'm':
                    surface_laby.blit(wall, (pos_x, pos_y), (40, 0, 20, 20))
                num_cell += 1
            num_row += 1

        pygame.display.flip()

        progress = 1
        while progress:
            progress = int(input())

    @property
    def grid_file_path(self):
        """Return the path of grid.txt,
           structure of the labyrinth"""

        path_file = path.dirname(path.dirname(__file__))
        return path.join(path_file, c.PATH_GRID, self.file)


if __name__ == "__main__":

    # py.init()

    window = py.display.set_mode((c.WINDOW_SIZE,
                                  c.WINDOW_SIZE))
    py.display.set_caption(c.TXT_TITLE)

    grille = Grid('grid.txt')
    grille.generate()
    print(grille.structure)
    grille.display(window)
