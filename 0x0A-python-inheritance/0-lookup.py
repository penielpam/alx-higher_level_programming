#!/usr/bin/python3

"""
This script defines a function for retrieving a list of available attributes and methods of an object.
"""

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    """
    return dir(obj)
