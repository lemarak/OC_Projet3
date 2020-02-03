#! /usr/bin/env python3
# coding: utf-8

import labyrinthe.constants as c
from labyrinthe.grid import *


def main():
    print("Hello Mac Gyver")
    grille = Grid('grid.txt')
    grille.generate()
    print(grille.structure)


if __name__ == "__main__":
    main()
