#!/usr/bin/python3
"""
test module for the module review
"""
import unittest
from models.review import Review
import models.review


class TestReview(unittest.TestCase):
    """ test class for the review """
    def test_mod_doc(self):
        """ checking for module documentation """
        self.assertIsNotNone(models.review.__doc__)

    def test_ls_doc(self):
        """ checking for class documentation """
        self.assertIsNotNone(Review.__doc__)

    def test_rev_text(self):
        """ checking if the attri text is string """
        review = Review()

        self.assertTrue(type(review.text) == str)


if __name__ == "__main__":
    unittest.main()
