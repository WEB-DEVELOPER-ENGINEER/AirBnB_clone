#!/usr/bin/python3
"""Class BaseModel"""
from datetime import datetime
from uuid import uuid4
import models
import json


class BaseModel:
    """construct"""

    def __init__(self, *args, **kwargs):
        """Initialization"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""
        return("[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__))

    def save(self):
        """updates the attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return a dictionary with keys/values of __dict__ of the instance"""
        aux_dict = self.__dict__.copy()
        aux_dict['__class__'] = self.__class__.__name__
        aux_dict['created_at'] = self.created_at.isoformat()
        aux_dict['updated_at'] = self.updated_at.isoformat()
        return aux_dict
