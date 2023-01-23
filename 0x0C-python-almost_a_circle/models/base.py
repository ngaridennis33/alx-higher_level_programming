#!/usr/bin/python3
# base.py
"""Script to define the Base model class"""


class Base:
    """ The Base class of the project.

        This class will manage id attribute and avoid duplicating code

        Attributes: 
        __nb_objects (Private class Attribute)

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize the constructor
        Args:
        int(id): The base identity
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
