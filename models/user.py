#!/usr/bin/python3
"""Defines a user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """A subclass that inherits from the Base class
    
    Attributes
        email (str): the email of the user
        password (str): password of the user
        first_name (str): first name of the user
        last_name (str): last name of the user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
