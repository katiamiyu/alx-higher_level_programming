#!/usr/bin/python3
"""
Module contain method
"""
import json


def from_json_string(my_str):
    """ converts str to object
    Arg(s):
        my_str
    """
    return json.loads(my_str)
