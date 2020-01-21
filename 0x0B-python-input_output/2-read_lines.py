#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    word_count = 0
    with open(filename, encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end="")
            return
        for a in f:
            if word_count < nb_lines:
                print(a, end="")
            word_count += 1
