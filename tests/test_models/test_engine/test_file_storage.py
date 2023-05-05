#!/usr/bin/python3
'''
    Tests for the file_storage module
'''


import os
import time
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class testFileStorage(unittest.TestCase):
    '''
        Testing the class FileStorage
    '''

    def setUp(self):
        '''
            Initialization
        '''
        self.storage = FileStorage()
        self.model = BaseModel()

    def tearDown(self):
        '''
            tearDown method
        '''
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_new(self):
        '''
            Tests the new method
        '''
        self.storage.new(self.model)
        key = str(self.model.__class__.__name__ + "." + self.model.id)
        self.assertTrue(key in self.storage._FileStorage__objects)