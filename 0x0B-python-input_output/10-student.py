#!/usr/bin/python3
"""
Module contain Student class
"""


class Student:
    """ class student
    """

    def __init__(self, first_name, last_name, age):
        """ initialises student class
        Args:
            first_name, last_name, age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ convert dictionary to json
        """
        if attrs is None:
            return self.__dict__
        elif isinstance(attrs, list):
            class_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    class_dict[key] = value
            return class_dict
