#!/usr/bin/python3
"""
module contains a class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle
    """
    def __init__(self, width, height):
        """
        initialising... method
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''
        return area of rectangle
        '''
        return self.__width * self.__height

    def __str__(self):
        '''
        string representation of class
        '''
        return(f"[Rectangle] {self.__width}/{self.__height}")
