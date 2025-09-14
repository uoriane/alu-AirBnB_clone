#!/usr/bin/python3
"""
AirBnB Clone Project - Place Model
Represents rental properties
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place model for rental properties
    Inherits all functionality from BaseModel
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
