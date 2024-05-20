#!/usr/bin/python3

from base_model import BaseModel

class User(BaseModel):
    """A subclass that inherits from the Base class"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
