#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for top in matrix:
        for i in range(len(top)):
            if i < len(top) - 1:
                print("{:d}".format(top[i]), end=" ")
            if i == len(top) - 1:
                print("{:d}".format(top[i]), end="")
        print("$")
