# coding: utf-8


from constants import *
from os import path
import pygame
from pygame.locals import *


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
        with open(self.filePath, 'r') as fil:  # open the file
            structure_grid = []
            for row in fil:     # read each row of the file
                line_grid = []
                for sprite in row:   # read each value in a row
                    if sprite != '\n':
                        line_grid.append(sprite)
                structure_grid.append(line_grid)
        self.structure = structure_grid

    def display(self):
        """
        display the labyrinth
        """
        wall = pygame.image.load()

    @property
    def filePath(self):
        path_file = path.dirname(path.dirname(__file__))
        return path.join(path_file, 'grid', self.file)


def main():
    print("Hello Mac Gyver")
    grille = Grid('grid.txt')
    grille.generate()
    print(grille.structure)


if __name__ == "__main__":
    main()
