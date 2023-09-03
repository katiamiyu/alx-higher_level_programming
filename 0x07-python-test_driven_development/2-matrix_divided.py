#!/usr/bin/python3
"""module contains function that divides all element of a matrix"""

def check_isint(row):
    """checks element type and return boolean"""
    return all(isinstance(el, int) for el in row)

def check_isfloat(row):
    """checks element type and return boolean"""
    return all(isinstance(el, float) for el in row)

def check_rowlen(matrix):
    """checks the length of each row of amatrix"""
    default = len(matrix[0])
    return all(len(row) == default for row in matrix)


def matrix_divided(matrix, div):
    """divides all the elements of matrix"""
    new_matrix = [[] for i in range(len(matrix))]

    for row in matrix:
        if not check_isint(row) and not check_isfloat(row):
            raise TypeError("matrix must be \
a matrix (list of lists) of integers/floats")
    if not check_rowlen(matrix):
        raise TypeError("each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            new_matrix[x].append(round(matrix[x][y] / div, 2))
    return new_matrix


