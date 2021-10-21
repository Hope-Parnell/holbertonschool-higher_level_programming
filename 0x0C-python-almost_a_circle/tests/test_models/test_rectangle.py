#!/usr/bin/python3
"""Unittests for Rectangle"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests the Rectangle class"""
    def testInit(self):
        """tests the initilization of rectangle"""
        r1 = Rectangle(3, 4)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(1, 5, 1, 2)
        self.assertEqual(r2.id, r1.id + 1)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 2)

        r3 = Rectangle(2, 3, id=142)
        self.assertEqual(r3.width, 2)
        self.assertEqual(r3.height, 3)
        self.assertEqual(r3.id, 142)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

        with self.assertRaises(TypeError):
            r4 = Rectangle()
            r5 = Rectangle(1)
            r4 = Rectangle("hello")
            r5 = Rectangle(1, "hello")
            r5 = Rectangle(1, 2, "hello")
            r5 = Rectangle(1, 2, 3, "hello")
            r5 = Rectangle(1, 2, 3, 4, "hello")

        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 1, id=0)
            r1 = Rectangle(0, 0, id=0)
            r1 = Rectangle(1, 0, id=0)
            r1 = Rectangle(-1, 1, id=0)
            r1 = Rectangle(1, -1, id=0)
            r1 = Rectangle(1, 1, -1, id=0)
            r1 = Rectangle(1, -1, 1, -1, id=0)

    def testSetters(self):
        """test rectangle setters"""
        r1 = Rectangle(1, 1)
        r1.id = 45
        self.assertEqual(r1.id, 45)
        r1.width = 3
        self.assertEqual(r1.width, 3)
        r1.height = 7
        self.assertEqual(r1.height, 7)
        r1.x = 4
        self.assertEqual(r1.x, 4)
        r1.y = 5
        self.assertEqual(r1.y, 5)
        r1.x = 0
        self.assertEqual(r1.x, 0)
        r1.y = 0
        self.assertEqual(r1.y, 0)

        with self.assertRaises(TypeError):
            r1.width = "hello"
            r1.height = True
            r1.x = [1, 2]
            r1.y = {3, 4}

        with self.assertRaises(ValueError):
            r1.width = 0
            r1.width = -1
            r1.height = 0
            r1.height = -1
            r1.x = -1
            r1.y = -1

    def testArea(self):
        """tests the area function"""
        r1 = Rectangle(4, 5, id=0)
        self.assertEqual(r1.area(), 20)
        r1.width = 1
        self.assertEqual(r1.area(), 5)
        r1.height = 4
        self.assertEqual(r1.area(), 4)

    def testUpdateArgs(self):
        """tests the update function with list"""
        r1 = Rectangle(1, 1, id=0)
        self.assertEqual(r1.id, 0)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r1.update(25)
        self.assertEqual(r1.id, 25)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r1.update(36, 5)
        self.assertEqual(r1.id, 36)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r1.update(25, 2, 3)
        self.assertEqual(r1.id, 25)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r1.update(3, 4, 5, 6)
        self.assertEqual(r1.id, 3)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 6)
        self.assertEqual(r1.y, 0)

        r1.update(4, 5, 6, 7, 8)
        self.assertEqual(r1.id, 4)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 6)
        self.assertEqual(r1.x, 7)
        self.assertEqual(r1.y, 8)

    def testUpdateKwargs(self):
        """Tests the update function with keywords"""
        r1 = Rectangle(1, 1, id=0)
        self.assertEqual(r1.id, 0)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r1.update(id=5)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r1.update(width=5, x=4, id=7)
        self.assertEqual(r1.id, 7)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 0)

        r1.update(width=4, x=5, id=4, y=2, height=3)
        self.assertEqual(r1.id, 4)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 2)

    def testCreate(self):
        """tests the create function from Base"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r2.id, 5)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)
