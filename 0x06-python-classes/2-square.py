#!/usr/bin/python3

"""Class Square"""


class Square:
    """Square gives the square of a value"""
    def __init__(self, size=0):
        """Initializing the Square class using the __init__ method
        Arqgs:
            size: is the size of the square"""
        self.__size = size

        type(size) is int
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
