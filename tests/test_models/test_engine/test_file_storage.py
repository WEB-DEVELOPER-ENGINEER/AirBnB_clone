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
import pep8


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
        self.test_len = 0
        if os.path.isfile("file.json"):
            self.test_len = len(self.storage.all())

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
        storage = FileStorage()
        instances_dic = storage.all()
        self.assertIsNotNone(instances_dic)
        self.assertEqual(type(instances_dic), dict)
        self.assertIs(instances_dic, storage._FileStorage__objects)

    def test_save_file_read(self):
        '''
            Testing the contents of the file file.json
        '''
        self.storage.save()
        self.storage.new(self.model)
        with open("file.json", encoding="UTF8") as fd:
            content = json.load(fd)
        self.assertTrue(type(content) is dict)

    def test_reload_empty(self):
        """
        Tests method: reload
        """
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

    def test_save(self):
        self.test_len = len(self.storage.all())
        a = BaseModel()
        a.save()
        self.assertEqual(len(self.storage.all()), self.test_len + 1)

    def test_pep8_FileStorage(self):
        """
            Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "Check pep8")
