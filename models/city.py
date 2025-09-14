#!/usr/bin/python3
"""
AirBnB Clone Project - City Model
Represents cities within states
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City model for urban areas
    Inherits all functionality from BaseModel
    """

    state_id = ""
    name = ""
