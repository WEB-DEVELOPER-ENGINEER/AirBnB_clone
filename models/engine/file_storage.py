#!/usr/bin/python3
"""Defines the FileStorage class"""
import json
from models.base_model import BaseModel
import os


class FileStorage:
    """serializes and deserializes instances to and from JSON file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj_class_name>.id"""
        FileStorage.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path"""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                dicts = json.load(f)
                FileStorage.__objects = {}
                for k, v in dicts.items():
                    obj = FileStorage.class_dict[v['__class__']](**v)
                    FileStorage.__objects[k] = obj
        except FileNotFoundError:
            return
