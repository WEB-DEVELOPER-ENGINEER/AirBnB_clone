#!/usr/bin/python3
"""Unittest for the review class"""
import pep8
import unittest
from models.review import Review


class TestBaseModelpep8(unittest.TestCase):
    """test pep8"""
    def test_pep8(self):
        """test for review file and test_review file"""
        style = pep8.StyleGuide(quiet=True)
        review_pep8 = "models/review.py"
        test_review_pep8 = "tests/test_models/test_review.py"
        result = style.check_files([review_pep8, test_review_pep8])
        self.assertEqual(result.total_errors, 0)


if __name__ == "__main__":
    unittest.main()
