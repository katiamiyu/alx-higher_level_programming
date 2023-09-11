#!/usr/bin/python3
"""
module contains an BaseGeometry class
"""

class BaseGeometry:
    """ this is a class
         methods:
         area
    """

    def area(self):
        """ gets area of shape
            args: void
            Return: raise exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ check type and value of entry
            Args:
            name - string
            value - integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
