#!/bin/usr/python3
def print_square(size):

    size_length = size

    if not isinstance(size_length, int):
        raise TypeError("size must be an integer")
    if size_length < 0 and type(size_length) is float:
        raise TypeError("size must be >= 0")
    if size_length == 0:
        print("")
    for a in range(size_length):
        for b in range(size_length):
            print("#", end="")
        print()
