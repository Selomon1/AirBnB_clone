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


clses = {"BaseModel": BaseModel, "User": User, "State": State,
         "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}


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
            classes: dictionary of classes
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return the object in dictionary """
        return self.__objects

    def new(self, obj):
        """ Set new object in the dictionary of objects """
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """ Convert objects to Json strings and save """
        dict_data = {}

        for key, value in self.__objects.items():
            dict_data[key] = value.to_dict()

        with open(self.__file_path, "w") as j:
            json.dump(dict_data, j)

    def reload(self):
        """ Deserialize Json strings to objects """
        try:
            with open(self.__file_path, 'r') as js:
                dso = json.load(js)
            for key in dso:
                self.__objects[key] = clses[dso[key]["__class__"]](**dso[key])

        except FileNotFoundError:
            pass
