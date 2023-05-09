#!/usr/bin/python3
"""Unittest for the amenity class"""
import pep8
import unittest
from models.amenity import Amenity


class TestBaseModelpep8(unittest.TestCase):
    """test pep8"""
    def test_pep8(self):
        """test for amenity file and test_amenity file"""
        style = pep8.StyleGuide(quiet=True)
        amenity_pep8 = "models/amenity.py"
        test_amenity_pep8 = "tests/test_models/test_amenity.py"
        result = style.check_files([amenity_pep8, test_amenity_pep8])
        self.assertEqual(result.total_errors, 0)


if __name__ == "__main__":
    unittest.main()
