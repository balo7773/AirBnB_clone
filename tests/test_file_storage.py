#!/usr/bin/python3
"""
Unittest for FileStorage class
"""

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up test method"""
        self.storage = FileStorage()
        self.file_path = FileStorage._FileStorage__file_path
        self.storage._FileStorage__objects = {}
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        """Tear down test method"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test that all() returns the __objects dictionary"""
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """Test that new() adds an object to __objects"""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test that save() properly saves objects to JSON file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open(self.file_path, 'r', encoding='utf-8') as file:
            content = json.load(file)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, content)

    def test_reload(self):
        """Test that reload() properly loads objects from JSON file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_reload_no_file(self):
        """Test that reload() handles missing file"""
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})


if __name__ == '__main__':
    unittest.main()
