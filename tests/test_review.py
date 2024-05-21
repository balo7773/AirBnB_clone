#!/usr/bin/python3
"""
Unittest for Review class
"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def setUp(self):
        """Set up test method"""
        self.review = Review()

    def test_instance_creation(self):
        """Test instance creation"""
        self.assertIsInstance(self.review, Review)

    def test_attributes(self):
        """Test attributes of Review"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_inheritance(self):
        """Test if Review inherits from BaseModel"""
        from models.base_model import BaseModel
        self.assertIsInstance(self.review, BaseModel)


if __name__ == '__main__':
    unittest.main()
