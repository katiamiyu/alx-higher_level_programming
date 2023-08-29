#!/usr/bin/python3
"""
This is a module that creates a Square class with initialization of Square size
for Python Classes.
This is task 5
"""


class Square:
    """
    This now a Square class with the size initialization and also
    this checks if the size variable is int and or less than 0.

    A new public instance method called area is implemented in order
    to calculate the area of a square.

    A new public instance method called my_print is implemented in
    order to print the square to stdout
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

    def my_print(self):
        if self.__size > 0:
            i = 0
            while i < self.__size:
                height = self.__size
                while height > 0:
                    print("#", end="")
                    height -= 1
                print()
                i += 1
        else:
            print()
