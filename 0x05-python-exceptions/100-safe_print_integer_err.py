#!/usr/bin/python3

from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (TypeError) as te:
        return False
        stderr.write("exception: {}\n".format(te))
    return True
