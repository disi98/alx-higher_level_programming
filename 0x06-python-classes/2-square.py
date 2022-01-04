#!/usr/bin/python3
"""defines a class called Square"""


class Square:

    """Represents a square"""

    def __init__(self, size=0):

        """Initializes the data
        Args:
            size: size of the square
        """

        self.__size = size

        type(size) is int
            if size < 0:
                raise ValueError("size must be >= 0")
            if type(size) is not int:
                raise TypeError("size must be an integer")

