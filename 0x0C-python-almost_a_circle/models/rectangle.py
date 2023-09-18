#!/usr/bin/python3
"""module contains rectangle class"""
from models.base import Base


class Rectangle(Base):
    """
    rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes instance of rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """ returns string representation
            of class and attributes
        """
        return (f"[{type(self).__name__}] ({self.id})"
                f" {self.x}/{self.y} - {self.width}/{self.height}")

    @property
    def width(self):
        """returns value"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns value"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns value"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets value"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns value"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets value"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area"""
        return (self.width * self.height)

    def display(self):
        """display rectangle shape"""
        for i in range(self.y):
            print("")
        x_axis = " " * self.x
        length = x_axis + "#" * self.width
        for i in range(self.height):
            print(f"{length}")

    def update(self, *args, **kwargs):
        """updates the values of attributes
            Args:
                args - lists of arguments
                kwargs - key word arguments
        """
        list_of_attr = ["id", "width", "height", "x", "y"]
        if list_of_attr and len(args) != 0:
            for i in len(args):
                setattr(self, list_of_attr[i], args[i])
        elif kwargs:
            for key in kwargs.keys():
                setattr(self, key, kwargs[key])
        else:
            raise ValueError("update: positional and/or keyword arg required")

    def to_dictionary(self):
        """returns the dictionary rep of Rectangle"""
        class_dict = self.__dict__
        rect_dict = {}
        for key, value in class_dict.items():
            if len(key) > 2:
                rect_dict[key[12:]] = value
            else:
                rect_dict[key] = value
        return rect_dict
