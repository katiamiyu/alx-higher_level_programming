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
    if isinstance(obj, a_class):
        return True
    obj_class = obj.__class__
    for p_class in obj_class.__bases__:
        if inherits_from(p_class, a_class):
            return True
    return False
