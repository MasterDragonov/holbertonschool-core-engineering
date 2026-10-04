#!/usr/bin/env python3
"""This module explores multiple inheritance with Fish, Bird, and FlyingFish."""


class Fish:
    """A class representing a generic fish."""

    def swim(self):
        """Prints swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Prints fish habitat information."""
        print("The fish lives in water")


class Bird:
    """A class representing a generic bird."""

    def fly(self):
        """Prints flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Prints bird habitat information."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A class representing a flying fish that inherits from both Fish and Bird."""

    def swim(self):
        """Overrides swim behavior for a flying fish."""
        print("The flying fish is swimming!")

    def fly(self):
        """Overrides fly behavior for a flying fish."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Overrides habitat information for a flying fish."""
        print("The flying fish lives both in water and the sky!")
