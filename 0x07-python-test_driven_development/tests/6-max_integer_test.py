#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class tests the max integer function"""

    def test_Proper(self):
        """test if max_integer finds correct max given valid input"""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([-5, -4, -3, -2]), -2)
        self.assertEqual(max_integer([-1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([74]), 74)
        self.assertEqual(max_integer([-43, 207, 42, 7]), 207)
    
    def test_Error(self):
        """Tests for errors from invalid input"""
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, 24)
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(Exception, max_integer, ["one", "two", "three", 4])
