#!/usr/bin/python3
"""Unittest for the place class"""
import pep8
import unittest
from models.place import Place


class TestBaseModelpep8(unittest.TestCase):
    """test pep8"""
    def test_pep8(self):
        """test for place file and test_place file"""
        style = pep8.StyleGuide(quiet=True)
        place_pep8 = "models/place.py"
        test_place_pep8 = "tests/test_models/test_place.py"
        result = style.check_files([place_pep8, test_place_pep8])
        self.assertEqual(result.total_errors, 0)


if __name__ == "__main__":
    unittest.main()
