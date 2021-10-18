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
        r0 = Rectangle(2, 3, -1, -5, 0)
        self.assertEqual(r0.width, 2)
        self.assertEqual(r0.height, 3)
        self.assertEqual(r0.id, 0)
        self.assertEqual(r0.x, -1)
        self.assertEqual(r0.y, -5)
        r3 = Rectangle(2, 3, -1, 3)
        self.assertEqual(r3.width, 2)
        self.assertEqual(r3.height, 3)
        self.assertEqual(r3.id, 3)
        self.assertEqual(r3.x, -1)
        self.assertEqual(r3.y, 3)
        r142 = Rectangle(2, 3, 2, *3, 142)
        self.assertEqual(r3.width, 2)
        self.assertEqual(r3.height, 3)
        self.assertEqual(r3.id, 142)
        self.assertEqual(r3.x, 2)
        self.assertEqual(r3.y, -3)
