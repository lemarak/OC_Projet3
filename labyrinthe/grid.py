# coding: utf-8

"""    Class Grid for create and display labyrinth    """

from os import path
import pygame
import pygame.locals

import constants
import functions as f


class Grid():
    """
    generate and display the labyrinth
    """

    def __init__(self, file):
        self.file = file
        self.structure = 0

    def generate(self):
        """
        generate the labyrinth
        """

        with open(self.grid_file_path, 'r') as fil:  # open the file
            structure_grid = []
            for row in fil:     # read each row of the file
                line_grid = []
                for sprite in row:   # read each value in a row
                    if sprite != '\n':
                        line_grid.append(sprite)
                structure_grid.append(line_grid)
        self.structure = structure_grid

    def display(self, window):
        """
        display the labyrinth
        """
        print(f.picture_file_path(constants.IMG_WALL))
        # wall = pygame.image.load(self.pictureFilePath(IMG_WALL)).convert()
        wall = pygame.image.load("./pictures/floor-tiles-20x20.png").convert()

        num_row = 0
        for row in self.structure:
            num_cell = 0
            for sprite in row:
                pos_x = num_cell * constants.SIZE_SPRITE
                pos_y = num_row * constants.SIZE_SPRITE
                if sprite == 'm':
                    window.blit(wall, (pos_x, pos_y), (40, 0, 20, 20))
                num_cell += 1
            num_row += 1

        pygame.display.flip()

        progress = 1
        while progress:
            progress = int(input())

    @property
    def grid_file_path(self):
        """Property who gives the path of grid.txt,
           structure of the labyrinth"""

        path_file = path.dirname(path.dirname(__file__))
        return path.join(path_file, constants.PATH_GRID, self.file)
