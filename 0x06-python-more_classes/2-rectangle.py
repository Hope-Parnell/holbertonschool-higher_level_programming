#!/usr/bin/python3
""" This is a simple module that creates a rectagle Class """


class Rectangle:
    """Creates a rectangle"""
    def __init__(self, width=0, height=0):
        """Initilizes width and height of rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """returns the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle

        Args:
            value (int): new width for the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle

        Args:
            value (int): new height for the rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectagle"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """returns the string definition of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            string = (("#" * self.__width) + "\n") * self.__height
            return string[:-1]
