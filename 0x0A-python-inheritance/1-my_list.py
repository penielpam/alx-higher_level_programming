#!/usr/bin/python3

"""Implements a custom list class MyList that inherits from the built-in list class."""

class MyList(list):
    """Overrides print_sorted method to print the list in sorted ascending order."""

    def print_sorted(self):
        """Prints the list in sorted ascending order."""
        print(sorted(self))

