#!/usr/bin/python3
# test_base.py
"""Defines unittest for base.py"""

import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBase_instance(unittest.TestCase):
    """Test the instantiation of the Base class"""
        
    def test_rectange_is_instance_base(self):
            self.assertIsInstance(Rectangle(10,2), Base)

    def test_no_args(self):
        with self.assertIsInstance(TypeError):
            Rectangle()

