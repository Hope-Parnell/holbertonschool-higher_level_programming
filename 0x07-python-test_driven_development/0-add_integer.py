#!/usr/bin/python3
"""simple addition module to learn how to create test files"""


def add_integer(a, b=98):
    """simple addition funtion

    Args:
        a (int): first number
        b (int): second number, defaults to 98
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
