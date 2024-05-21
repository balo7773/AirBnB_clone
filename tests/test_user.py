#!/usr/bin/python3
"""
Unittest for User class
"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def setUp(self):
        """Set up test method"""
        self.user = User()

    def test_instance_creation(self):
        """Test instance creation"""
        self.assertIsInstance(self.user, User)

    def test_attributes(self):
        """Test attributes of User"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_inheritance(self):
        """Test if User inherits from BaseModel"""
        from models.base_model import BaseModel
        self.assertIsInstance(self.user, BaseModel)


if __name__ == '__main__':
    unittest.main()
