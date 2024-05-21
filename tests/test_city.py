#!/usr/bin/python3
"""
Unittest for City class
"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def setUp(self):
        """Set up test method"""
        self.city = City()

    def test_instance_creation(self):
        """Test instance creation"""
        self.assertIsInstance(self.city, City)

    def test_attributes(self):
        """Test attributes of City"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_inheritance(self):
        """Test if City inherits from BaseModel"""
        from models.base_model import BaseModel
        self.assertIsInstance(self.city, BaseModel)


if __name__ == '__main__':
    unittest.main()
