#!/usr/bin/python3
"""
module contains function that checks exactly instamce of class
"""


def is_same_class(obj, a_class):
    """ checks if object is exactly an instance of class
        Args:
            obj - first argument(instance)
            a_class - class object(blueprint)
    """
    return type(obj) is a_class
