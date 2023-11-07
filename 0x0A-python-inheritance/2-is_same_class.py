#!/usr/bin/python3

"""
This script defines a function for checking whether an object is an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """Check if an object is precisely an instance of a given class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to be matched with the type of obj.
    Returns:
        True if obj is exactly an instance of a_class, otherwise False.
    """
    if type(obj) == a_class:
        return True
    return False
