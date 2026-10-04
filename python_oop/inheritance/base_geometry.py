#!/usr/bin/env python3
"""This module defines a BaseGeometry class for geometric modeling."""


class BaseGeometry:
    """A foundational class representing base geometric behavior."""

    def area(self):
        """Raises an Exception because the method is abstract at this level.

        Raises:
            Exception: Always raised with an unimplemented message.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that an input value is a strictly positive integer.

        Args:
            name (str): The label or identifier for the value.
            value (int): The data value to inspect.

        Raises:
            TypeError: If the value is not an exact integer type.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
