#!/usr/bin/python3
""" """
from tests import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ Test model for amenity"""

    def __init__(self, *args, **kwargs):
        """ attributes"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)