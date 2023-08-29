#!/usr/bin/python3
"""
This is a module that creates a Square class and initialization of Square size
for Python Classes
This is task 3 and that is all this module will handle
"""


class Square:
    """
    This now a Square class with the size initialization and also
    this checks if size variable is an int or less than 0.

    A new public instance method is added  to calculate the
    area of a square.
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """This calculates area of the square"""
        return self.__size * self.__size
