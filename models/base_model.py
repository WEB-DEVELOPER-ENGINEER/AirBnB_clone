#!/usr/bin/python3
"""Class BaseModel"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """construct"""

    def __init__(self, *args, **kwargs):
        """Construct"""
        if kwargs != {}:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    val = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, val)
                    continue
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""
        stri = "[{:s}] ({:s}) {}"
        return stri.format(type(self).__name__, self.id, self.__dict__)

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
