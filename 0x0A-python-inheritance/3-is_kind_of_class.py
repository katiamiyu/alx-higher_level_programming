#!/usr/bin/python3
"""
module contains function that checks instamce of class
"""


def is_kind_of_class(obj, a_class):
    """ checks if object is an instance of class
        Args:
            obj - first argument(instance)
            a_class - class object(blueprint)
    """
    return isinstance(obj, a_class)
