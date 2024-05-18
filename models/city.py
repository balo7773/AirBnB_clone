#!/usr/bin/python3
"""Module that defines the City class.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
