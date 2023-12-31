#!/usr/bin/python3
"""
add two object files together using json
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def to_list():
    """ add json objects
        Args:
            void
    """
    try:
        my_list = load_from_json_file("add_item.json")
        for i in range(1, len(sys.argv)):
            my_list.append(sys.argv[i])
        save_to_json_file(my_list, "add_item.json")
    except FileNotFoundError:
        with open("add_item.json", "w") as f:
            f.write("[]")
        my_list = load_from_json_file("add_item.json")
        for i in range(1, len(sys.argv)):
            my_list.append(sys.argv[i])
        save_to_json_file(my_list, "add_item.json")


if __name__ == "__main__":
    to_list()
