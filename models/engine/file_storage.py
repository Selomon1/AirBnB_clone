#!/usr/bin/python3


import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}
        
    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        dict_data = {}

        for key, value in FileStorage.__objects.items():
            dict_data[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as j:
            json.dump(dict_data, j)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as j:
                deserilized_obj = json.load(j)
                for key, obj in deserilized_obj.items():
                    nameof_class = obj["__class__"]
                    del obj["__class__"]
                    FileStorage.__objects[key] = eval(nameof_class + "(**obj)")

        except FileNotFoundError:
            pass
