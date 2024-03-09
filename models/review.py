#!/usr/bin/python3
"""module that defines a class review"""
from models.base_model import BaseModel

class Review(BaseModel):
    """class Review attributes"""

    place_id: str = ""
    user_id: str = ""
    text: str = ""