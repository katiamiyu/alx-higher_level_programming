#!/usr/bin/python3

from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as te:
        stderr.write("exception: {}".format(te))
        return False
    return True
