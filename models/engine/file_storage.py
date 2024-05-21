#!/usr/bin/python3

"""Defining the file" storage"""
import json
import os
from importlib import import_module
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """Json file"""
    
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """Returns the dicitonary object"""
        return self.__objects
    
    def new(self, obj):
        """Set in __objects the obj with key"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializing the object to the Json file"""
        with open(self.__file_path, 'w') as f:
            json_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(json_objects, f)

    
    def reload(self):
        """Deserializes the JSON file to __objects if the JSON file exists."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                json_objects = json.load(f)
                for key, obj_dict in json_objects.items():
                    class_name = obj_dict['__class__']
                    module_name = "models.base_model"
                    obj_class = getattr(import_module(module_name), class_name)
                    self.__objects[key] = obj_class(**obj_dict)
                    
    def classes(self):
        """Return a dictionary of valid classes"""
        return {
            'BaseModel': BaseModel,
            'User': User
        }
