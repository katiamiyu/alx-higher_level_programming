#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value/1
    except Exception as e:
        return (False)
    else:
        return (True)
