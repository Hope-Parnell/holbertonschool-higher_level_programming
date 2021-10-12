#!/usr/bin/python3
"""Module includes print_square function for 
learning to make test files
"""


def print_square(size):
    """prints a square of size
    
    Args:
        size(int): length of the sides of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    
    for x in range(size):
        print("#" * size)
