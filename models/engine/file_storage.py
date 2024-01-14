#!/usr/bin/python3
"""Serializes instances to a JSON file and.

deserializes JSON file to instances.
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class_dict = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "Amenity": Amenity,
    "City": City,
    "Review": Review,
    "State": State
}


class FileStorage:
    """FileStorage - A base class for file storage using JSON.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary to store serialized objects.

    Methods:
        all(self): Returns the dictionary __objects.
        new(self, obj): Sets in __objects the obj with key <obj class name>.id.
        save(self): Serializes __objects to the JSON file (path: __file_path).
        reload(self): Deserializes the JSON file to __objects
                      (only if the JSON file (__file_path) exists).
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of objects."""
        return type(self).__objects

    def new(self, obj):
        """Set new obj in __objects dictionary."""
        if obj.id in type(self).__objects:
            print("exists")
            return
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        type(self).__objects[key] = obj
        # OR
        # type(self).__objects[obj.id] = obj

    def save(self):
        """Serialize __objects to the JSON file (path: __file_path)."""
        new_dict = []
        for obj in type(self).__objects.values():
            new_dict.append(obj.to_dict())
            # for key, obj in type(self).__objects.items():
            #    new_dict[key] = obj.to_dict()
        with open(type(self).__file_path, "w", encoding='utf-8') as file:
            json.dump(new_dict, file)
            # OR
            # with open(type(self).__file_path, "w", encoding="utf-8") as file:
            #   json.dump([obj.to_dict() for obj in self.all().values()], file)

    def reload(self):
        """Deserialize the JSON file to __objects if it exists."""
        if os.path.exists(type(self).__file_path) is True:
            return
            try:
                with open(type(self).__file_path, "r") as file:
                    new_obj = json.load(file)
                    for key, val in new_obj.items():
                        obj = self.class_dict[val['__class__']](**val)
                        type(self).__objects[key] = obj
            except Exception:
                pass
