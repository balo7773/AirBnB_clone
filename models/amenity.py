#!/usr/bin/python3
"""module that defines the Amenity class, inheriting from BaseModel.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""
