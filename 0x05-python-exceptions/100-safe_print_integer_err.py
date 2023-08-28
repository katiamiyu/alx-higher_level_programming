#!/usr/bin/python3

from sys import stderr


def safe_print_integer_err(value):
    flag = none
    try:
        print("{:d}".format(value))
        flag = True
    except (TypeError) as te:
        flag = False
        stderr.write("exception: {}\n".format(te))
    return flag
