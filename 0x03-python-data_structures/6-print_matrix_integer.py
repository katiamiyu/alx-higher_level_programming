#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        idx = len(row) - 1
        x = 0
        while x <= idx:
            print("{:d}".format(row[x]), end="")
            if x != idx:
                print(" ", end="")
            x += 1
        print()
