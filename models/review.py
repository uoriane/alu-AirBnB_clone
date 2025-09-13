#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class for AirBnB clone project"""
    place_id = ""
    user_id = ""
    text = ""