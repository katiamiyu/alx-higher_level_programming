#!/usr/bin/python3
"""
This is a module that creates a Square class with initialization of Square size
for Python Classes.
This is task 2
"""


class Square:
    """
    This is a Square class with the size initialization and
    1.  checks if the size variable is an int or less than 0.
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
