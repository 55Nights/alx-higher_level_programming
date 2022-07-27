#!/usr/bin/python3

""" Define a class rectangle"""


class Rectangle:

    """
    A class rectangle

    -----------------
    Attributes
      ----
      width : private must be int
      heigth: private must be int

    Methods
     ----
      width(self) : getter for width
      width(self, value) : setter for width
      height(self) : getter for height
      height(self, value) : setter for height
    """
    def __init__(self, width=0, height=0):
        if isinstance(width, int) is False:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if isinstance(height, int) is False:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        """ gets the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the value of width """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ gets the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the value of height """
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the area of a circle """

        return (self.__width * self.__height)

    def perimeter(self):
        """ Returns the perimeter """

        return (2 * (self.__width + self.__height))
