#!/usr/bin/python3
"""Public class attributes:
    name: string - empty string"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''
        Amenity class that inherits from BaseModel class
    '''
    name = ""
