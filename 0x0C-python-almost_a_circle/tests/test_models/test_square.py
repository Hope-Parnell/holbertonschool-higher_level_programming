#!/usr/bin/python3
"""Unittests for Square Class"""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """tests the Square class"""
    def testInit(self):
        """test Square initilization"""
        s1 = Square(1)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.size, s1.width)
        self.assertEqual(s1.size, s1.height)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s1 = Square(2, 1, 3)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.size, s1.width)
        self.assertEqual(s1.size, s1.height)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 3)

        with self.assertRaises(TypeError):
            s1 = Square()
            s1 = Square("hi")
            s1 = Square(1, "hi")
            s1 = Square(1, 1, "hi")

        with self.assertRaises(ValueError):
            s1 = Square(-2)
            s1 = Square(0)
            s1 = Square(1, -1)
            s1 = Square(1, 1, -1)

    def testSetter(self):
        """test the size setter"""
        s1 = Square(1)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.size, s1.width)
        self.assertEqual(s1.size, s1.height)

        s1.size = 4
        self.assertEqual(s1.size, 4)
        self.assertEqual(s1.size, s1.width)
        self.assertEqual(s1.size, s1.height)

        with self.assertRaises(TypeError):
            s1.size = "hi"
            s1.size = True
            s1.size = {1, 2, 3}
            s1.size = {'one': 1, 'two': 2, 'three': 3}
            s1.size = (1, 2, 3)
            s1.size = [1, 2, 3]

        with self.assertRaises(ValueError):
            s1.size = -1
            s1.size = 0

    def testCreate(self):
        """tests the create function from Base"""
        s1 = Square(1, 2, 3, 4)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(s2.id, 4)
        self.assertEqual(s2.size, 1)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
