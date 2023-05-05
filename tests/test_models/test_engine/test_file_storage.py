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

    def test_objects_type(self):
        '''
            Tests the type of objects
        '''
        self.storage.new(self.model)
        key = str(self.model.__class__.__name__ + "." + self.model.id)
        value = self.storage._FileStorage__objects[key]
        self.assertIsInstance(self.model, type(value))

    def test_save_exists(self):
        '''
            Tests that the file file.json gets created
        '''
        self.storage.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_all_method(self):
        '''
            Tests the return type of the method all
        '''
        storage_all = self.storage.all()
        self.assertIsInstance(storage_all, dict)

    def test_reaload_method_without_file(self):
        '''
            Tests that if the file doesn’t exist, no exception is raised
        '''
        try:
            self.storage.reload()
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_reload_empty(self):
        '''
            Tests method reload
        '''
        a_storage = FileStorage()
        try:
            os.remove("file.json")
        except Exception:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(a_storage.reload(), None)
