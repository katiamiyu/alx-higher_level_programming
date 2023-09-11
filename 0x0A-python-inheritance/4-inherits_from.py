#!/usr/bin/python3
"""
module contains function that checks inhertance of class
"""


def inherits_from(obj, a_class):
    """ checks if object is a subclass of class
        Args:
            obj - first argument(instance)
            a_class - class object(blueprint)
    """
    return issubclass(obj, a_class)
