#!/usr/bin/python3
""" A unittest class for base_model"""


import models
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel_to_dict(unittest.TestCase):
    """Unittest case for the to_dict method in BaseModel class"""

    def test_to_dict_instance(self):
        instance = BaseModel()
        result = instance.to_dict()
        self.assertIsInstance(result, dict)


if __name__ == '__main__':
    unittest.main()