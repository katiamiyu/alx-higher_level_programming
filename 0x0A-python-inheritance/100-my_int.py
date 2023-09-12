#!/usr/bin/python3
"""
Module class MyInt
"""


class MyInt(int):
    """
    class MyInt blueprint
    """

    def __eq__(self, other):
        """
        equality magic method
        """
        return (float(self) != float(other))

    def __ne__(self, other):
        """
        non equality magics method
        """
        return float(self) == float(other)
