#!/usr/bin/python3
def number_of_lines(filename=""):
    word_count = 0
    with open(filename, encoding='utf-8') as f:
        for a in f:
            word_count += 1
    return word_count
