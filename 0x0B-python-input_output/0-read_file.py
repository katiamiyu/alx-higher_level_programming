#!/usr/bin/python3
"""
module contains a readfile method
"""


def read_file(filename=""):
    """
    reads text from filr and display on screen
    """
    with open(filename, "r", encoding = "utf-8") as f:
        print(f.read())
