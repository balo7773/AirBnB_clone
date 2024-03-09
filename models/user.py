#!/usr/bin/python3
"""module that defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """class user attribute"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""