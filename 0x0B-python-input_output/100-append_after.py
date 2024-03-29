#!/usr/bin/python3
"""a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to be inserted.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
