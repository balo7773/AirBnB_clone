#!/usr/bin/python3
"""
Unittest for State class
"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def setUp(self):
        """Set up test method"""
        self.state = State()

    def test_instance_creation(self):
        """Test instance creation"""
        self.assertIsInstance(self.state, State)

    def test_attributes(self):
        """Test attributes of State"""
        self.assertEqual(self.state.name, "")

    def test_inheritance(self):
        """Test if State inherits from BaseModel"""
        from models.base_model import BaseModel
        self.assertIsInstance(self.state, BaseModel)


if __name__ == '__main__':
    unittest.main()
