#!/usr/bin/python3
"""Public class attributes:
state_id: string - empty string: it will be the State.id
"""
from models.base_model import BaseModel


class City(BaseModel):
    '''
        A class that defines a city and inherits from BaseModel class
    '''
    state_id = ""
    name = ""
