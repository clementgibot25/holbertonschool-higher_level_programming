#!/usr/bin/python3

"""
Module reads file and prints it to stdout
"""


def read_file(filename=""):
    with open(filename, "r") as f:
        print(f.read(), end="")


if __name__ == "__main__":
    read_file("0-read_file.py")
