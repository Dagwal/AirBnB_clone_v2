#!/usr/bin/python3
"""User Module"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Declaring the the class name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
