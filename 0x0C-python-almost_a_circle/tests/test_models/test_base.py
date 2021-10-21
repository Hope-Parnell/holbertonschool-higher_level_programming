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
        self.assertEqual(base2.id, 2)
        base3 = Base()
        self.assertEqual(base3.id, 3)
        base0 = Base(0)
        self.assertEqual(base0.id, 0)
        base4 = Base()
        self.assertEqual(base4.id, 4)
        base5 = Base()
        self.assertEqual(base5.id, 5)
        base6 = Base(-5)
        self.assertEqual(base6.id, -5)
        base7 = Base(43)
        self.assertEqual(base7.id, 43)
        base7.id = 7
        self.assertEqual(base7.id, 7)

    def test_to_json_string(self):
        """tests to_json_string function"""
        list_dict = [{'id': 8}, {'id': None}, {'id': 358}, {'id': -16}]
        self.assertEqual(Base.to_json_string(list_dict),
                         '[{"id": 8}, {"id": null}, {"id": 358}, {"id": -16}]')
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_from_json_string(self):
        """tests the from_json_string function"""
        test_json = Base.to_json_string(
            [{'id': 8}, {'id': None}, {'id': 358}, {'id': -16}])
        self.assertEqual(Base.from_json_string(test_json),
                         [{"id": 8}, {"id": None}, {"id": 358}, {"id": -16}])
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        with self.assertRaises(TypeError):
            Base.from_json_string()
