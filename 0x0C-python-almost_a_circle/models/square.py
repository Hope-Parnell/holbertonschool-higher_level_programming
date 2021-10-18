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
