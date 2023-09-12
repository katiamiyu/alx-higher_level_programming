#!/usr/bin/python3
"""
Module defines writefile mrthod
"""


def write_file(filename="", text=""):
    """
    opens a file and writes a fixed number of text
    Args:
        filename: name of file
        text: string to be written
    Return: numbrr of char
    """
    with open(filename, "w", encoding="utf-8") as f:
        n_of_char = f.write(text)
        return n_of_char
