#!/usr/bin/python3
def read_file(filename: str = "") -> None:
    """
    Reads the contents of a UTF-8 encoded text file and outputs it to stdout.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None
    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
