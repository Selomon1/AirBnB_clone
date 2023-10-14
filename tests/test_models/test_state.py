#!/usr/bin/python3
"""
test module for the state module
"""
import unittest
from models.state import State
import models.state


class TestState(unittest.TestCase):
    """ test class for the State """
    def test_mod_doc(self):
        """ checking module documentation """
        self.assertIsNotNone(models.state.__doc__)

    def test_cls_doc(self):
        """ checking class documentation """
        self.assertIsNotNone(State.__doc__)

    def test_state_name(self):
        """ checking the attr name if it is string """
        state = State()

        self.assertTrue(type(state.name) == str)


if __name__ == "__main__":
    unittest.main()
