#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, mode ='w', encoding='utf-8') as f:
        file1 = f.write(text)
    return file1
