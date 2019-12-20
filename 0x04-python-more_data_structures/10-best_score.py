#!/usr/bin/python3
def best_score(a_dictionary):
    for key in a_dictionary:
        score = a_dictionary[key]
        if score == "":
            return None
        else:
            return score
