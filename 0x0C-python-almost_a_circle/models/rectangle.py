#!/usr/bin/python3
# rectangle.py
"""Class Rectangle inherits from Base"""

from models.base import Base

class Rectangle(Base):
    """The Rectangle class of the object

    Private Attributes:
        __width
        __height
        __x
        __y

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize the constructor
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self):
        return self.__width

    @property 
    def height(self):
        return self.__height

    @height.setter
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self):
        return self.__y