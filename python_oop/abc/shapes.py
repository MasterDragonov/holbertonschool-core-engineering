#!/usr/bin/env python3
"""This module defines shapes and demonstrates interface duck typing."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """An abstract base class representing a geometric shape interface."""

    @abstractmethod
    def area(self):
        """Calculates and returns the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates and returns the perimeter of the shape."""
        pass


class Circle(Shape):
    """A concrete class representing a circle."""

    def __init__(self, radius):
        """Initializes a new Circle instance.

        Args:
            radius (int, float): The radius of the circle.
        """
        self.__radius = radius

    def area(self):
        """Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """Calculates and returns the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """A concrete class representing a rectangle."""

    def __init__(self, width, height):
        """Initializes a new Rectangle instance.

        Args:
            width (int, float): The width of the rectangle.
            height (int, float): The height of the rectangle.
        """
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates and returns the area of the rectangle.

        Returns:
            int, float: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle.

        Returns:
            int, float: The perimeter of the rectangle.
        """
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """Prints the area and perimeter of a shape object using duck typing.

    Args:
        shape (Shape): An object responding to the area and perimeter interface.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
