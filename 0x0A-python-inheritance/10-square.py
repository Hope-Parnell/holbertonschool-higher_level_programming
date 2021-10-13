#!/usr/bin/python3
"""Module contains the Class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class is a square that inherits Rectangle"""

    def __init__(self, size):
        """initilizes the square

        Arg:
            size(int): length of square's sides
        """
        super().integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """returns area of the square"""
        return super().area()
