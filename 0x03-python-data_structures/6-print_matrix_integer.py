#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    x = 0
    y = 0
    for i in matrix:
        x = 0
        while x < len(i):
            if x < (len(i) - 1):
                print("{:d}".format(i[x]), end=' ')
            else:
                print("{:d}".format(i[x]), end='')
            x = x + 1
        print()
