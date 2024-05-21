#!/usr/bin/python3
"""
Unittest for Amenity class
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def setUp(self):
        """Set up test method"""
        self.amenity = Amenity()
        

    def test_instance_creation(self):
        """Test instance creation"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_name_initialization(self):
        """Test default name attribute"""
        self.assertEqual(self.amenity.name, "")

    def test_attribute_assignment(self):
        """Test attribute assignment"""
        self.amenity.name = "Pool"
        self.assertEqual(self.amenity.name, "Pool")

    def test_to_dict(self):
        """Test to_dict method"""
        self.amenity.name = "WiFi"
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['name'], "WiFi")
        self.assertEqual(amenity_dict['__class__'], 'Amenity')

    def test_str(self):
        """Test __str__ method"""
        self.amenity.name = "Jacuzzi"
        string = str(self.amenity)
        self.assertIn("[Amenity] (", string)
        self.assertIn("name: 'Jacuzzi'", string)


if __name__ == '__main__':
    unittest.main()
