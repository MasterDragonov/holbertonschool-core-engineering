#!/usr/bin/env python3
"""This module defines a Rectangle class extending BaseGeometry."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A representation of a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Initializes a new Rectangle instance with validation.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates and returns the area of the rectangle.

        Returns:
            int: The calculated area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """Defines the customized string representation of the instance.

        Returns:
            str: Description of the rectangle in the specified format.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
