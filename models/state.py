#!/usr/bin/python3
"""
State class inherited from BaseModel module
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class inherited from BaseModel
    Attributes:
            name (str): users state name
    """
    name = ""
