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

    def area(self):

        """  returns the current square area """
        return (self.__size * self.__size)

    @property
    def size(self):

        """ This is a getter method """

        return self.__size

    @size.setter
    def size(self, value):
        """ This is the setter method """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
