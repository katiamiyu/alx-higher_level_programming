#!/usr/bin/python3
"""
module contains an BaseGeometry class
"""


class BaseGeometry:
    """
    class
    """
    def area(self):
        """
        gets area of shape
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        check type and value of entry
        """
        if type(value) !=  int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
