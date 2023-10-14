#!/usr/bin/python3
"""
City class inherited from BaseModel class Module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class inherited from BaseModel class
    Attributes:
            state_id (str): users state id of the city
            name (str): city name
    """
    state_id = ""
    name = ""
