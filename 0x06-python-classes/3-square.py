#!/usr/bin/python3

"""Class Square that returns a square of a value"""


class Square:
    """The class square gives a square of a value"""
    def __init__(self, size=0):
        """The square class is initialized using the __init__ method
        Args:
            size: is the size of the value to be squared
            """
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >=0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
        
    def area(self):
       
        """Returns The arear of the size"""

        return (self.__ize * self.__size)
