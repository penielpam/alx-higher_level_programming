#!/usr/bin/python3
"""
function that creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename):
    if filename[-4::] != 'json':
        return "Not a JSON file"
    """crate and object from a "JSON file" """
    with open(filename, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)
