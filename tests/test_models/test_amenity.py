#!/usr/bin/python3
"""
unit test for the amenity class
"""
import unittest
from models.amenity import Amenity
import models.amenity


class TestUser(unittest.TestCase):
    """
    test class for the amenity class
    """
    def test_mod_doc(self):
        """ module documentation """
        self.assertIsNotNone(models.amenity.__doc__)

    def test_cls_doc(self):
        """ class documentation """
        self.assertIsNotNone(Amenity.__doc__)

    def test_amen_name(self):
        """ checking for string """
        amenity = Amenity()
        self.assertTrue(type(amenity.name) == str)


if __name__ == "__name__":
    unittest.main()
