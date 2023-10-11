#!/usr/bin/python3
"""
A module that defines all common attributes/methods
"""


from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    A class that defines all classes
    """
    def __init__(self, *args, **kwargs):
        """
        instantiation of instance attributes
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    conv_obj = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, conv_obj)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            models.storage.new(self)

    def save(self):
        """
        saves each time an instance attribute is updateded
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all key or value of insatnce
        """
        dict_data = {}
        dict_data["__class__"] = self.__class__.__name__

        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dict_data[key] = value.isoformat()
            else:
                dict_data[key] = value

        return dict_data

    def __str__(self):
        """
        returns the string representation
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
