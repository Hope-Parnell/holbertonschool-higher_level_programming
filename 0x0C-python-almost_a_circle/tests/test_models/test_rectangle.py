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
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(1, 5, 1, 2)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 2)
        r142 = Rectangle(2, 3, id=142)
        self.assertEqual(r142.width, 2)
        self.assertEqual(r142.height, 3)
        self.assertEqual(r142.id, 142)
        self.assertEqual(r142.x, 0)
        self.assertEqual(r142.y, 0)
