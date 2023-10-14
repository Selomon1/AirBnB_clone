#!/usr/bin/python3
"""
test module for the user module
"""
import unittest
from models.user import User
import models.user


class TestUser(unittest.TestCase):
    """ test class for the User """
    def test_mod_doc(self):
        """ checking module documentation """
        self.assertIsNotNone(models.user.__doc__)

    def test_cls_doc(self):
        """ checking class documentation """
        self.assertIsNotNone(User.__doc__)

    def test_user_fname(self):
        """ checking first_name of the user if it is string """
        user = User()

        self.assertTrue(type(user.first_name) == str)

    def test_usr_lname(self):
        """ checking last_name of the user for string """
        user = User()

        self.assertTrue(type(user.last_name) == str)


if __name__ == "__main__":
    unittest.main()
