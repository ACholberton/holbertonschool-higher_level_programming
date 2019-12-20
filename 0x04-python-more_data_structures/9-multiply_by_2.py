#!usr/bin/python3
def multiply_by_2(a_dictionary):
    dictionary = a_dictionary.copy()
    dictionary = {key: a * 2 for key, a in dictionary.items()}
    return dictionary
