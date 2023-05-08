#!/usr/bin/python3
"""Unittest for the city class"""
import pep8
import unittest
from models.city import City


class TestBaseModelpep8(unittest.TestCase):
    """test pep8"""
    def test_pep8(self):
        """test for city file and test_city file"""
        style = pep8.StyleGuide(quiet=True)
        city_pep8 = "models/city.py"
        test_city_pep8 = "tests/test_models/test_city.py"
        result = style.check_files([city_pep8, test_city_pep8])
        self.assertEqual(result.total_errors, 0)


if __name__ == "__main__":
    unittest.main()
