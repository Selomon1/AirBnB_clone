#!/usr/bin/python3
"""
FileStorage class module
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    FileStorage class: a storage engine for AirBnB clone
    Methods class:
            all: return the object
            new: set new object and update
            save: convert objects to Json strings
            reload: deserilize json string to instance
    Attributes:
            __file_path: the file that saves the object
            __objects: dictionary of the instanization of objects
            dict_data: dictionary of classes
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return the object in dictionary """
        return FileStorage.__objects

    def new(self, obj):
        """ Set new object in the dictionary of objects """
        FileStorage.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """ Convert objects to Json strings and save """
        dict_data = {}

        for key, value in FileStorage.__objects.items():
            dict_data[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as j:
            json.dump(dict_data, j)

    def reload(self):
        """ Deserialize Json strings to objects """
        try:
            with open(FileStorage.__file_path, 'r') as j:
                deserilized_obj = json.load(j)
                for key, obj in deserilized_obj.items():
                    nameof_class = obj["__class__"]
                    del obj["__class__"]
                    FileStorage.__objects[key] = eval(nameof_class + "(**obj)")

        except FileNotFoundError:
            pass
