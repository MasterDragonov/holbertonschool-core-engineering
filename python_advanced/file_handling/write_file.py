#!/usr/bin/env python3
"""Module that contains a function to write a string to a file."""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 text file and returns characters written.

    Args:
        filename (str): The name of the file to write to. Defaults to "".
        text (str): The text content to write into the file. Defaults to "".

    Returns:
        int: The number of characters successfully written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
