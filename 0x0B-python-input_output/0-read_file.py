#!/usr/bin/python3
"""
Contains the read_file function that is to be excicuted
"""


def read_file(filename=""):
    """""reads a text file(UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
    read_file()    
