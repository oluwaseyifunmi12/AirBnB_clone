#!/usr/bin/python3
"""A base class from which other classes inherit"""

import uuid
from datetime import datetime

class BaseModel():
    """A Base class model"""
    
    def __init__(self):
        """Initializing BaseMOdle instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
    def __str__(self):
        """Return string representation of BaseMOdel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the current attribute with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the BAseMOdle instance"""
        result = self.__dict__.copy()
        result['__class__'] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['update_at'] = self.updated_at.isoformat()
        return result