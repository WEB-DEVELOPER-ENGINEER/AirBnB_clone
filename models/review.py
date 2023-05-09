#!/usr/bin/python3
"""Public class attributes:
    place_id: string - empty string: it will be the Place.id
    user_id: string - empty string: it will be the User.id
    text: string - empty string"""
from models.base_model import BaseModel


class Review(BaseModel):
    '''
        Review class that inherits from BaseModel class
    '''
    place_id = ""
    user_id = ""
    text = ""
