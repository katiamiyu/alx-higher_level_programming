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
        else:
            class_dict = {}
            for li in attrs:
                if li in self.__dict__.keys():
                    class_dict[li] = self.__dict__[li]
            return class_dict
