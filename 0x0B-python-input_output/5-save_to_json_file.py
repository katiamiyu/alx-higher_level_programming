#!/usr/bin/python3
"""
method writes an obj to file using json
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes obj to file
    Args:
        my_obj, filename
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
