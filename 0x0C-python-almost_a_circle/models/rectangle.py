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
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle

        Arg:
            value: new height for the rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the y of the rectangle

        Arg:
            value: new y for the rectangle
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def update(self, *args, **kwargs):
        """updates the rectangle's attributes

        Arg:
            args: list of new attributes [id, width, height, x, y]
        """
        i = len(args)
        if i > 0:
            if i >= 1:
                self.id = args[0]
            if i >= 2:
                self.width = args[1]
            if i >= 3:
                self.height = args[2]
            if i >= 4:
                self.x = args[3]
            if i >= 5:
                self.y = args[4]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def area(self):
        """gives the area of a rectangle"""
        return self.__height * self.__width

    def display(self):
        """displays the rectangle"""
        print("\n" * self.y, end="")
        for j in range(self.height):
            print(" " * self.y + "#" * self.width)

    def __str__(self):
        """string representation of Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def to_dictionary(self):
        """creates a dictionary for a rectangle"""
        return {'id': self.id, 'width': self.width,
                'height': self.height, 'x': self.x, 'y': self.y}
