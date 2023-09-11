#!/usr/bin/python3
"""
module contains Rectangle class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Rectangle class blueprint
    """
    def __init__(self, width, height):
        """
        init doc
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
