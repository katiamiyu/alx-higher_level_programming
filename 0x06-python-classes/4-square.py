#!/usr/bin/python3
"""
This is a module that creates a Square class with initialization of Square size
for Python classes.
This is task 4
"""


class Square:
    """
    This now a Square class with the size initialization and also
    this checks if the size variable is an int and or less than 0.

    A new public instance method is added in order to calculate
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

    @property
    def size(self):
        """This is the class property getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """This is the class property setter"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
