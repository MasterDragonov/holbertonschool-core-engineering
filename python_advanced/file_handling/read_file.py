#!/usr/bin/env python3
"""Module that contains a function to read and print a file's content."""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints its content to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to "".
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
