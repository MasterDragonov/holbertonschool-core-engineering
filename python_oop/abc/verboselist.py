#!/usr/bin/env python3
"""This module defines a custom list that prints verbose notifications."""


class VerboseList(list):
    """A custom list subclass that logs notifications when items change."""

    def append(self, item):
        """Appends an item to the list and prints a notification.

        Args:
            item: The element to add to the end of the list.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extends the list with items from an iterable and logs it.

        Args:
            iterable: A collection of elements to append to the list.
        """
        items_list = list(iterable)
        num_items = len(items_list)
        super().extend(items_list)
        print("Extended the list with [{}] items.".format(num_items))

    def remove(self, item):
        """Removes the first occurrence of an item and logs it beforehand.

        Args:
            item: The element to remove from the list.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pops an item from the specified index and logs it beforehand.

        Args:
            index (int): The index of the item to remove. Defaults to -1.

        Returns:
            The popped element.
        """
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
