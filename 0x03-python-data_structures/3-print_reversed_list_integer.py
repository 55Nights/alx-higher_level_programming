#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        return my_list
    else:
        i = (len(my_list) - 1)
        while i >= 0:
            print("{:d}" .format(my_list[i]))
            i = i - 1
