#!/usr/bin/python3
def write_file(filename="", text=""):
    # Open the file in write mode using 'with' statement
    with open(filename, "w", encoding="utf-8") as file:
        # Write the text to the file and get the number of characters written
        num_chars_written = file.write(text)
    # Return the number of characters written
    return num_chars_written

