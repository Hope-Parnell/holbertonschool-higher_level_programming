#!/usr/bin/python3
"""Module contains the Rectangle Class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initilizes the rectagle

        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
            x: vertical location of the rectangle
            y: horizontal location of the rectangle
            id: the id for the rectangle
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        if type(y) is not int:
            raise TypeError("x must be an integer")
        if y < 0:
            raise ValueError("x must be >= 0")

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle

        Arg:
            value: new width for the rectangle
        """
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def width(self, value):
        """sets the height of the rectangle

        Arg:
            value: new height for the rectangle
        """
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x of the rectangle

        Arg:
            value: new x for the rectangle
        """
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @x.setter
    def y(self, value):
        """sets the y of the rectangle

        Arg:
            value: new y for the rectangle
        """
        self.__y = value


