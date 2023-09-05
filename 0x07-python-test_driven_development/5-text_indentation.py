#!/usr/bin/python3
"""
module with text indentation function
"""


def text_indentation(text):
    """
    text indentation function
    args:
        text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    s = [".", "?", ":"]
    lines = []
    current_line = ""
    for char in text:
        current_line = current_line + char
        if char in s:
            lines.append(current_line.strip())
            current_line = ""
    lines.append(current_line.strip())
    for line in lines:
        if line == lines[len(lines) - 1]:
            print(line, end="")
        else:
            print(line + "\n")
