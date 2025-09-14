#!/usr/bin/python3
"""
AirBnB Clone Project - User Model
Represents user accounts
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User model for account management
    Inherits all functionality from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
