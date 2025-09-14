#!/usr/bin/python3
"""
AirBnB Clone Project - Review Model
Represents user reviews
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review model for user feedback
    Inherits all functionality from BaseModel
    """

    place_id = ""
    user_id = ""
    text = ""
