#!/usr/bin/python3

""" class with private attr"""


class Square:

    """ init method """
    def __init__(self, size=0):
        """The constructor of class"""
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
