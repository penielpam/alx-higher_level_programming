#!/usr/bin/python3

"""
Contains a function for checking if an object inherits from a specific class.
"""

def inherits_from(obj, a_class):
    """
    Checks if an object inherits from a specific class.

    Args:
        obj (object): The object to check for inheritance.
        a_class (type): The class to compare inheritance with.

    Returns:
        bool: True if obj is an instance of a subclass of a_class, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class

