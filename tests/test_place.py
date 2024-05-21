#!/usr/bin/python3
"""
Unittest for Place class
"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""

    def setUp(self):
        """Set up test method"""
        self.place = Place()

    def test_instance_creation(self):
        """Test instance creation"""
        self.assertIsInstance(self.place, Place)

    def test_attributes(self):
        """Test attributes of Place"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_inheritance(self):
        """Test if Place inherits from BaseModel"""
        from models.base_model import BaseModel
        self.assertIsInstance(self.place, BaseModel)


if __name__ == '__main__':
    unittest.main()
