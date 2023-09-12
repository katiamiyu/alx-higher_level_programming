#!/usr/bin/python3
"""
defines append write function
"""


def append_write(filename="", text=""):
    """ writes text to file
        Args:
            filename - name of filr
            text - string to accept
        Return:
            no_of_char
    """
    with open(filename, "a", encoding = "utf-8") as f:
        n_of_char = f.write(text)
        print(n_of_char)
