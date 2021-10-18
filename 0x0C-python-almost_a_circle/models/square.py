#!/usr/bin/python3
"""Module contains the Square Class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initilizes the square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """gets the size of a sqare"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size of the Square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the square"""
        if len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']


