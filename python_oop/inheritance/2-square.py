#!/usr/bin/env python3
"""This module defines a Square class extending Rectangle."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """A representation of a square using the Rectangle class."""

    def __init__(self, size):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the side of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Defines the customized string representation of the Square instance.

        Returns:
            str: Description of the square in the specified format.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
