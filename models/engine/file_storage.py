#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    """Serializes instances to a JSON file & deserializes back"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of all objects"""
        return self.__objects

    def new(self, obj):
        """Add new object to __objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON file"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
            for key, val in obj_dict.items():
                class_name = val["__class__"]
                if class_name == "BaseModel":
                    self.__objects[key] = BaseModel(**val)
                # If you have other classes, add them here
        except FileNotFoundError:
            pass

