#!/usr/bin/python3
"""
AirBnB Clone Project - Amenity Model
Represents property amenities
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity model for property features
    Inherits all functionality from BaseModel
    """

    name = ""
