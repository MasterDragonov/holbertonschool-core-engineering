#!/usr/bin/env python3
"""This module defines abstract and concrete representations of animals."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """An abstract base class representing a generic animal."""

    @abstractmethod
    def sound(self):
        """An abstract method that must be overridden by all subclasses."""
        pass


class Dog(Animal):
    """A concrete class representing a dog, inheriting from Animal."""

    def sound(self):
        """Returns the specific vocal sound of a dog.

        Returns:
            str: The string "Bark".
        """
        return "Bark"


class Cat(Animal):
    """A concrete class representing a cat, inheriting from Animal."""

    def sound(self):
        """Returns the specific vocal sound of a cat.

        Returns:
            str: The string "Meow".
        """
        return "Meow"
