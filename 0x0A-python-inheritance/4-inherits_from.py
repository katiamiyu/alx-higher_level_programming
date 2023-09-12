#!/usr/bin/python3
"""
module contains function that checks inhertance of class
"""


def inherits_from(obj, a_class):
    """
    checks if object is a subclass of class
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
