#!/usr/bin/python3
"""unittests for models/user.py"""
import os
import models
import unittest
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    '''
        tests instantiation of the User class
    '''
    def test_no_args(self):
        self.assertEqual(User, type(User()))

    def test_new_user_is_stored(self):
        self.assertIn(User(), models.storage.all().values())

    def test_email_type(self):
        self.assertEqual(str, type(User.email))

    def test_password_type(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_type(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_type(self):
        self.assertEqual(str, type(User.last_name))
