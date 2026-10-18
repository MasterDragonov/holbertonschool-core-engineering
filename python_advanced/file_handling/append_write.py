#!/usr/bin/env python3
"""Module that contains a function to append a string to a file."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF-8 text file.

    Creates the file if it does not exist.

    Args:
        filename (str): The name of the file to modify. Defaults to "".
        text (str): The text content to append. Defaults to "".

    Returns:
        int: The number of characters successfully appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
