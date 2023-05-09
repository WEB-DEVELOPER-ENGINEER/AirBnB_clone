#!/usr/bin/python3
"""Unittest for the city class"""
import pep8
import unittest
from models.state import State


class TestBaseModelpep8(unittest.TestCase):
    """test pep8"""
    def test_pep8(self):
        """test for state file and test_state file"""
        style = pep8.StyleGuide(quiet=True)
        state_pep8 = "models/state.py"
        test_state_pep8 = "tests/test_models/test_state.py"
        result = style.check_files([state_pep8, test_state_pep8])
        self.assertEqual(result.total_errors, 0)


if __name__ == "__main__":
    unittest.main()
