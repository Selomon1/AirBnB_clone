#!/usr/bin/python3
"""
test module for the console module
"""
import unittest
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """ test class for the console HBNBCommand """
    def test_prom(self):
        """ checking if the prompt if it is is the same """
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)


if __name__ == "__main__":
    unittest.main()
