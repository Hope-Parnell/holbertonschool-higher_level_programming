#!/usr/bin/python3
"""This module contains a rectangle class that inherits
from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class for rectangles"""
    def __init__(self, width, height):
        """initilizes the width and height for the rectangle

        Args:
            width(int): width of Rectangle
            height(int): height of Rectangle
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        __width = width
        __height = height
