#!/usr/bin/python3
"""module contains Rectangle class"""


class Rectangle:
    """
    creates a Rectangle object
    """
    def __init__(self, width=0, height=0):
        """ init new instance
            Args:
            width (int) with of the rectangle instance
            height (int) height of the rectangle instance
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter property
            Return:
            value of the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter property
            Args:
            value (int) the new width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter property
            Return:
            value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter property
            Args:
            value (int) the new height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ gets the area
            Return:
                area
        """
        return self.width * self.height

    def perimeter(self):
        """ gets the perimeter
            Return:
                perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """ triangle represented
            drawn with #
            Return:
                rec_str
        """
        rec_str = ""
        if self.width == 0 or self.height == 0:
            return rec_str
        rec = "#" * self.width + "\n"
        for i in range(self.height):
            rec_str += rec
        return rec_str

    def __repr__(self):
        """ Return:
            a string representation of instance
            of rectangle
        """
        return (f"Rectangle({self.width}, {self.height})")
