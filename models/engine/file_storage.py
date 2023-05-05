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
        if (os.path.isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path) as f:
                FileStorage.__objects = json.load(f)
                for o in FileStorage.__objects.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
