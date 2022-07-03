#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    #  a function that prints a matrix of integers
    for element in matrix:
        print(" ".join("{:d}".format(a) for a in element))
