#!/usr/bin/python3
"""module contains square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializrs instance of square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns string representation of squares"""
        return (f"[{type(self).__name__}] ({self.id})"
                f" {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """get value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """ set value of size
            Args:
                value - length of sides
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """porpulate attr usings args and kwargs"""
        list_of_attr = ["id", "size", "x", "y"]
        if list_of_attr and len(args) > 0:
            for i in args:
                setattr(self, list_of_attr[i], args[i])
        elif kwargs:
            for key in kwargs.keys():
                setattr(self, key, kwargs[key])
        else:
            raise ValueError("update: positional and/or keyword arg required")

    def to_dictionary(self):
        """returns the dictionary rep of square"""
        class_dict = self.__dict__
        square_dict = {}
        for key, value in class_dict.items():
            if len(key) > 2:
                key = key[12:]
                if key in ["width", "height"]:
                    key = "size"
                square_dict[key] = value
            else:
                square_dict[key] = value
        return square_dict
