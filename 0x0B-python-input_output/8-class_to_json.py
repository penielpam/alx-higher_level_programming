#!/usr/bin/python3
"""a Python class-to-JSON function."""


def class_to_json(obj):
    """Returns the dictionary's represntation of a simple data structure."""
    return obj.__dict__
