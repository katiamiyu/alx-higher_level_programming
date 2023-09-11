#!/usr/bin/python3
"""
module contain class Square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square with methods
    """
    def __init__(self, size):
        """
        initialising square obj
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        get area of squaere
        """
        return self.__size ** 2
