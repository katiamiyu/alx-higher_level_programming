#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return []
    count = len(my_list)-1
    new_list = []
    for i in range(count, -1, -1):
        print("{:d}".format(my_list[i]))
