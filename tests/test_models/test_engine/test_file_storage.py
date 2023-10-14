#!/usr/bin/python3
"""
test module for the file_storage module
"""
import unittest
from uuid import uuid4
from models.engine.file_storage import FileStorage
import models


class TestFileStorage(unittest.TestCase):
    """ test class for the FileStorage """
    def test_mod_doc(self):
        """ checking for the module documentaion """
        self.assertIsNotNone(models.engine.file_storage.__doc__)

    def test_cls_doc(self):
        """ checking for the class FileStorage """
        self.assertIsNotNone(FileStorage.__doc__)

    def test_file_reload(self):
        """ test reload """
        stor = FileStorage()
        stors = stor.all()
        self.assertTrue(len(stors) > 0)


if __name__ == "__main__":
    unittest.main()
