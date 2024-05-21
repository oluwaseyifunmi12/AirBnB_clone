#!/usr/bin/python3
""" A unittest class for base_model"""

import unittest
from io import StringIO
import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Unittest case for methods in BaseModel class"""

    def test_save_method(self):
        captured_output = StringIO()
        sys.stdout = captured_output

        model = BaseModel()
        model.save()

        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue().strip(), "OK")

    def test_to_dict_instance(self):
        instance = BaseModel()
        result = instance.to_dict()
        self.assertIsInstance(result, dict)
        self.assertEqual(result['__class__'], 'BaseModel')
        self.assertEqual(result['created_at'], instance.created_at.isoformat())
        self.assertEqual(result['updated_at'], instance.updated_at.isoformat())

    def test_str_method(self):
        model = BaseModel()
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_str)


if __name__ == '__main__':
    unittest.main()
