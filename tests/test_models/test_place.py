#!/usr/bin/python3
"""
test module for the place module
"""
import unittest
from models.place import Place
import models.place


class TestPlace(unittest.TestCase):
    """ test class for the Place class """
    def test_mod_doc(self):
        """ checking module documentation """
        self.assertIsNotNone(models.place.__doc__)

    def test_cls_doc(self):
        """ checking class documentaion """
        self.assertIsNotNone(Place.__doc__)

    def test_place_name(self):
        """ checking the attrib name if it is string """
        place = Place()

        self.assertTrue(type(place.name) == str)


if __name__ == "__main__":
    unittest.main()
