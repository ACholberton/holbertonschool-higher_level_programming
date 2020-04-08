#!/usr/bin/python3
"""
function that finds a peak in a list of unsorted integers
"""

def find_peak(list_of_integers):
    """function to find the peak of the integers"""
    list_n = list_of_integers
    if list_n is None:
        return None

    if len(list_n) == 0:
        return None

    if len(list_n) == 1:
        return (list_n[0])

    middle = len(list_n) // 2
    for peak in list_n:
        if peak > 0 and list_n[middle - 1]:
            return peak
        elif peak > 0 and list_n[middle + 1]:
            return peak
