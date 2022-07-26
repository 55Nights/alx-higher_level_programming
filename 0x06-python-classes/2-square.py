#!/usr/bin/python3

""" class with private attr"""


class Square:

    """ init method """
    def __init__(self, size=0):
        try:
            if isinstance(size, int) is not True:
                raise TypeError
            elif size < 0:
                raise ValueError
            else:
                self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
