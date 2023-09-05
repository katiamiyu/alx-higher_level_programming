#!/usr/bin/python3
"""module defines locked class"""


class LockedClass:
    """locked class, prevents user from creating instances
       attributes  except for attribute first_name
    """

    __slots__ = ["first_name"]
