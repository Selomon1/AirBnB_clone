#!/usr/bin/python3
"""
User class inherited from BaseModel module
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class inherited from BaseModel
    Attibutes:
            email (str):  user email address
            password (str): user password
            first_name (str): users first name
            last_name (str): users last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
