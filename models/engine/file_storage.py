#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
                elif class_name == "User":
                    self.__objects[key] = User(**val)
                elif class_name == "State":
                    self.__objects[key] = State(**val)
                elif class_name == "City":
                    self.__objects[key] = City(**val)
                elif class_name == "Amenity":
                    self.__objects[key] = Amenity(**val)
                elif class_name == "Place":
                    self.__objects[key] = Place(**val)
                elif class_name == "Review":
                    self.__objects[key] = Review(**val)
        except FileNotFoundError:
            pass