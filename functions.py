#! /usr/bin/env python3
# coding: utf-8

"""    project functions    """

from os import path

import constants as c


def picture_file_path(img_file):
    """    returns the full path of the image file    """

    path_file = path.dirname(path.dirname(path.dirname(__file__)))
    print(path_file)
    return path.join(path_file, c.PATH_PICTURES, img_file)
