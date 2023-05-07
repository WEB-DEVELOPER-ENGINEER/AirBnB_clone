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
        '''
            tests when passing no args
        '''
        self.assertEqual(User, type(User()))

    def test_new_user_is_stored(self):
        '''
            tests if the new user is stored
        '''
        self.assertIn(User(), models.storage.all().values())

    def test_email_type(self):
        '''
            tests the type of the attr: email
        '''
        self.assertEqual(str, type(User.email))

    def test_password_type(self):
        '''
            tests the type of the attr: password
        '''
        self.assertEqual(str, type(User.password))

    def test_first_name_type(self):
        '''
            tests the type of the attr: first_name
        '''
        self.assertEqual(str, type(User.first_name))

    def test_last_name_type(self):
        '''
            tests the type of the attr: last_name
        '''
        self.assertEqual(str, type(User.last_name))

    def test_User_attributes(self):
        '''
            Test that the attributes exist
        '''
        user = User()
        self.assertTrue("email" in user.__dir__())
        self.assertTrue("first_name" in user.__dir__())
        self.assertTrue("last_name" in user.__dir__())
        self.assertTrue("password" in user.__dir__())
