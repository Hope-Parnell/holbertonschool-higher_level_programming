#!/usr/bin/python3
"""This module creates a class with the private attribute size
and checks for valid size input
"""


class Square:
    """create a class Square and use __init__ to set size"""
    def __init__(self, size=0):
        '''initilizes the square after checking for valid input

        Args:
            size (int): the size of the square
        '''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
