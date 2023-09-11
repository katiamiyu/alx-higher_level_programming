#!/usr/bin/python3
"""
module contains class  mylist that inherites from
class list with function print_sorted
"""


class MyList(list):
    """ class Mylist, a subclass of list
        use the init function of list
    """

    def print_sorted(self):
        """ function gets the sorted list
            Arg: void
            Return: sorted list
        """
        new_list = sorted(self)
        print(new_list)
