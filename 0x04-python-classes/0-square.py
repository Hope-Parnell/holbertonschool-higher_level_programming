#!/usr/bin/python3
"""This module creates a class with the private attribute size"""


class Square:
    """create a class Square and use __init__ to set size"""
    def __init__(self, size):
        '''initilizes the square
        Args:
            size (int): the size of the square
        '''
        self.__size = size
