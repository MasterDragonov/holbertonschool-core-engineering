#!/usr/bin/env python3
"""This module demonstrates composition using mixins with a Dragon class."""


class SwimMixin:
    """A mixin that provides swimming functionality to a creature."""

    def swim(self):
        """Prints swimming capability."""
        print("The creature swims!")


class FlyMixin:
    """A mixin that provides flying functionality to a creature."""

    def fly(self):
        """Prints flying capability."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A class representing a dragon, combining swimming and flying mixins."""

    def roar(self):
        """Prints the unique roaring action of a dragon."""
        print("The dragon roars!")
