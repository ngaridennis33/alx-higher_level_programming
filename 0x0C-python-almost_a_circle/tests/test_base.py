#!/usr/bin/python3
# test_base.py
"""Defines unittest for base.py"""

import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBase_instance(unittest.TestCase):
    """Test the instantiation of the Base class"""

    def test_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)
