#!/usr/bin/python3
"""
Module contains  function pascal_triangle
"""


def pascal_triangle(n):
    """
    gets list of number representing
    pascal triagle
    Args:
         n: degree of triagele
    Returns:
        list
    """
    res = [[1]]
    if n <= 0:
        return []
    if n == 1:
        return res

    def getthenext(prev):
        new_row = [1]
        a = len(prev)
        i = 0
        while i <= a - 2:
            ele = prev[i] + prev[i + 1]
            new_row.append(ele)
            i += 1
        new_row.append(1)
        return new_row

    x = 0
    while x <= n - 2:
        res.append(getthenext(res[x]))
        x += 1
    return res
