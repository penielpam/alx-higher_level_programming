#!/usr/bin/python3

"""
This module defines the MyList class, a custom list subclass with added functionality.
"""

class MyList(list):
    """
    MyList is a subclass of the built-in list class, enhancing its functionality.

    Attributes:
        None

    Methods:
        print_sorted(): Prints the elements of the list in sorted order.
    """

    def __init__(self):
        """
        Initializes a MyList object by calling the parent list's constructor.
        """
        super().__init()

    def print_sorted(self):
        """
        Prints the elements of the list in sorted order.
        """
        print(sorted(self))

