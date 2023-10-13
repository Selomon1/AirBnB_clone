#!/usr/bin/python3
"""
Place class inherited from BaseModel class module
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class inherited from BaseModel class
    Attributes:
            city_id (str): users city id
            user_id (str): user id
            name (str): the name of the place
            description (str): description of the place
            number_rooms (int): number of rooms
            number_bathrooms (int): number of bathroom in the house
            max_guest (int): number of guests that can accommedate
            price_by_night (int): the price per a night
            latitude (float): latitude coordination of the place or hotel
            longitude (float): longitude coordination of the place or hotel
            amenity_ids (str): amenity ids associated with the hotel or place
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
