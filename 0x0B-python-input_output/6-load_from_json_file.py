#!/usr/bin/python3
"""
function that creates an Object from a “JSON file”
"""

import json


def load_from_json_file(filename: str):
    with open(filename, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)
