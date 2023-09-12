#!/usr/bin/python3
"""
method load an obj from file using json
"""
import json


def load_from_json_file(filename):
    """
    loads obj from file
    Args:
        filename
    """
    with open(filename, "r") as f:
        return json.load(f)
