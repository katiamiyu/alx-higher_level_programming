#!/usr/bin/python3


import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except BaseException:
        sys.stderr.write("Exception: {}".format(sys.exc_info()[1]) + "\n")
        return None
