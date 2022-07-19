#!/usr/bin/python3

class Square:

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

    def area(self):
        """ calculates the area of a square """
        return (self.__size * self.__size)
