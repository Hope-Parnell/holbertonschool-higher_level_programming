#!/usr/bin/python3
"""Module is a unittest for the base module"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """tests the Base class"""
    def testIDSet(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base()
        self.assertEqual(base2, 2)
        base3 = Base()
        self.assertEqual(base3.id, 3)
        base0 = Base(0)
        self.assertEqual(base0.id, 0)
        base4 = Base()
        self.assertEqual(base4.id, 4)
        base5 = Base()
        self.assertEqual(base5.id, 5)
