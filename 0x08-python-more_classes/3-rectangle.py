#!/usr/bin/python3
"""
Project: 0x08. Python - More Classes and Objects
Task: 3
"""


class Rectangle:
    """"
    Class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
    """

    def __init__(self, width=0, height=0):
        """
        Constructor
        """

        self.width = width
        self.height = height

    def __str__(self):
        """
        Print the rectangle with the character #
        """

        str = ""
        if self.__width == 0 or self.__height == 0:
            return str
        else:
            for row in range(self.__height):
                str += "#" * self.__width
                if row < (self.__height - 1):
                    str += "\n"
        return str

    @property
    def width(self):
        """
        Getter the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter the width
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter the height
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the rectangle perimeter

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
