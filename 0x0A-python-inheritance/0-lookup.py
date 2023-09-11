#!/usr/bin/python3
"""
Module contains lookup function
"""


def lookup(obj):
    """ Function gets the list of attributes of obj
        Args:
        obj - python object
        Return: list of attributes
    """
    return dir(obj)
