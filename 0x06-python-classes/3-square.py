#!/usr/bin/python3
"""Square."""


class Square:
    """define a square."""

    def __init__(self, size=0):
        """constructor.
        Args:
            size:square side length.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """square area."""
        return (self.__size * self.__size)
