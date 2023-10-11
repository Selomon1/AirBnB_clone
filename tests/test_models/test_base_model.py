#!/usr/bin/python3
"""
Tests the Base Model module
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
import uuid


class TestBaseModel(unittest.TestCase):
    """ Test the BaseModel  class """

    def setUp(self):
        pass

    def test_mod_doc(self):
        """ Testing the documentation of module """
        self.assertIsNotNone(models.base_model.__doc__)

    def test_cls_doc(self):
        """ Testing  the documentation of class """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_meth_doc(self):
        """ Testing the documentation of methods """
        methods = [
                BaseModel.__init__,
                BaseModel.__str__,
                BaseModel.save,
                BaseModel.to_dict,
                ]
        for met in methods:
            self.assertIsNotNone(met.__doc__)
    
    def test_init_attr(self):
        """ Test id of the object """
        test_mod = BaseModel()
        test_mod1 = BaseModel()

        # checking whether id exists, is string and NULL
        self.assertTrue(hasattr(test_mod, "id"))
        self.assertIsNotNone(test_mod.id)
        self.assertIsInstance(test_mod.id, str)

        # Checking whether id is uuid
        self.assertTrue(uuid.UUID(test_mod.id))

        # Checking whether two instances have the same id
        self.assertNotEqual(test_mod.id, test_mod1.id)

    def test_created_at(self):
        """ Tests created at """
        self.assertTrue(hasattr(test_mod, "created_at"))
        self.assertIsNotNone(test_mod.created_at)
        self.assertIsInstance(test_mod.created_at, datetime)

    def test_updated_at(self):
        """ Testing updated at """
        self.assertTrue(hasattr(test_mod, "updated_at")
        self.assertIsNotNone(test_mod.updated_at)
        self.assertIsInstance(test_mod.updated_at, datetime)

    def test_str_output(self):
        """ Testing if it prints the correct output """
        str_out = "[BaseModel] ({}) {}".format(test_mod.id, test_mod.__dict__)
        self.assertEqual(str(test_mod), str_out)

        old_update = test_mod.updated_at
        test_mod.save()
        self.assertGreater(test_mod.updated_at, old_update)

    def test_kwargs_input(self):
        """ Testing kwargs initialzation of the class """
        dic = {
            "id": "test_id"
            "created_at": "2023-10-11T05:27:50.784510",
            "updated_at": "2023-10-11T05:28:37.684534",
            "name": "Sol_Ermi",
            "value": 23,
            }
        test_mod = BaseModel(**dic)

        self.assertEqual(test_mod.id, "test_id")
        self.assertEqual(test_mod.name, "Sol_Ermi")
        self.assertEqual(test_mod.value, 23)
        self.assertIsInstance(test_mod.created_at, datetime)
        self.assertIsInstance(test_mod.updated_at, datetime)

    def test_to_dict_type(self):
        """ Testing data type after converted to_dict """
        test_mod = BaseModel()
        test_mod.name = "Sol_Ermi"
        test_mod.age = "baby"
        test_mod.number = 23

        test_dic = test_mod.to_dict()

        self.assertIsInstance(test_dic, dict)
        self.assertEqual(test_dic["__class__"], "BaseModel")
        self.assertEqual(test_dic["id"], test_mod.id)
        self.assertEqual(test_dic["name"], "Sol_Ermi")
        self.assertEqual(test_dic["age"], "baby")
        self.assertEqual(test_dic["number"], 23)

    def test_save_args(self):
        """ Testing the save methods """
        test_mod = BaseModel()
        with self.assertRaises(TypeError):
            test_mod.save(None)

if __name__ == "__main__":
    unittest.main()
