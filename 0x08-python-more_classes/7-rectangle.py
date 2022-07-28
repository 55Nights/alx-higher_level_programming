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
      number_of_instances : public class attr

    Methods
     ----
      width(self) : getter for width
      width(self, value) : setter for width
      height(self) : getter for height
      height(self, value) : setter for height
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ initializes when an instance is created """
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

        Rectangle.number_of_instances += 1

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
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """ prints rectangle """
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            s = ""
            for i in range(self.__height):
                for x in range(self.__width):
                    s += str(self.print_symbol)
                if i < (self.__height - 1):
                    s += '\n'
                else:
                    pass
        return s

    def __repr__(self):
        return 'Rectangle({self.width}, {self.height})'.format(self=self)

    def __del__(self):
        """ prints a message whe instance of rectangle is destroyed"""
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
        else:
            Rectangle.number_of_instances = 0
        print("Bye rectangle...")
