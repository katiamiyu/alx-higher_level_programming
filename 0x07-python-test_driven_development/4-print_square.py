#!/usr/bin/python3
"""Module contains function that prints squares"""

def print_square(size):
    """returns square of length size"""
    if not isinstance(size, int) or isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")

