#!/usr/bin/env python3
"""This module defines a Rectangle class that inherits from BaseGeometry."""
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
