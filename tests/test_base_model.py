#!/usr/bin/python3
"""
Unittest for BaseModel class
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
import uuid


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up test method"""
        self.model = BaseModel()

    def test_instance_creation(self):
        """Test instance creation"""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_unique_id(self):
        """Test that each instance has a unique id"""
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)

    def test_str(self):
        """Test __str__ method"""
        string = str(self.model)
        self.assertIn("[BaseModel] (", string)
        self.assertIn("id", string)
        self.assertIn("created_at", string)
        self.assertIn("updated_at", string)

    def test_save(self):
        """Test save method updates 'updated_at'"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_kwargs(self):
        """Test instance creation from kwargs"""
        model_dict = self.model.to_dict()
        model2 = BaseModel(**model_dict)
        self.assertEqual(model2.id, self.model.id)
        self.assertEqual(model2.created_at, self.model.created_at)
        self.assertEqual(model2.updated_at, self.model.updated_at)
        self.assertIsNot(self.model, model2)

    def test_invalid_kwargs(self):
        """Test instance creation with invalid kwargs"""
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)


if __name__ == '__main__':
    unittest.main()
