# coding: utf-8


from os import path
import pygame
from pygame.locals import *
from constants import *


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
        with open(self.gridFilePath, 'r') as fil:  # open the file
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
        print(self.pictureFilePath(IMG_WALL))
        # wall = pygame.image.load(self.pictureFilePath(IMG_WALL)).convert()
        wall = pygame.image.load("./pictures/floor-tiles-20x20.png").convert()

        num_row = 0
        for row in self.structure:
            num_cell = 0
            for sprite in row:
                x = num_cell * SIZE_SPRITE
                y = num_row * SIZE_SPRITE
                if sprite == 'm':
                    window.blit(wall, (x, y), (40, 0, 20, 20))
                num_cell += 1
            num_row += 1

        pygame.display.flip()

        progress = 1
        while progress:
            progress = int(input())

    def pictureFilePath(self, imgFile):
        path_file = path.dirname(path.dirname(path.dirname(__file__)))
        print(path_file)
        return path.join(path_file, PATH_PICTURES, imgFile)

    @property
    def gridFilePath(self):
        path_file = path.dirname(path.dirname(__file__))
        return path.join(path_file, PATH_GRID, self.file)


def main():
    print("Hello Mac Gyver")
    pygame.init()

    window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption(TXT_TITLE)

    grille = Grid('grid.txt')
    grille.generate()
    print(grille.structure)
    grille.display(window)


if __name__ == "__main__":
    main()
