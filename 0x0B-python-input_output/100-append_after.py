#!/usr/bin/python3
"""
Module contain function append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """
    containing a specifique character
    """
    with open(filename) as f:
        lines = f.readlines()
    for index, line in enumerate(lines):
        if search_string in line:
            lines.insert(index + 1, new_string)
    with open(filename, "w") as f:
        f.write("".join(lines))
