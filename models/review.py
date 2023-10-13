#!/usr/bin/python3
"""
Review class inherited from BaseModel module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class inherited from BaseModel class
    Attributes:
            place_id (str): id of the place to be reviewed
            user_id (str): user id who review about the place
            text (str): the review text content or space
    """
    place_id = ""
    user_id = ""
    text = ""
