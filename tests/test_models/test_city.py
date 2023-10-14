#!/usr/bin/python3
"""
test for the city module
"""
import unittest
from models.city import City
import models.city


class TestCity(unittest.TestCase):
    """ testing the city class """
    def test_mod_doc(self):
        """ tests for module's documentation """
        self.assertIsNotNone(models.city.__doc__)

    def test_cls_doc(self):
        """ tests for class' documentation """
        self.assertIsNotNone(City.__doc__)

    def test_cit_name(self):
        """ checking city name for string """
        city = City()

        self.assertTrue(type(city.name) == str)


if __name__ == "__main__":
    unittest.main()
