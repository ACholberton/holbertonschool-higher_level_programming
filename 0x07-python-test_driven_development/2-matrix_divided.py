#!/usr/bin/python3
def matrix_divided(matrix, div):
    errmessage = "matrix must be a matrix (list of lists) of integers/floats" 
    if not isinstance(matrix, list) or matrix == [] or matrix == [[]]:
        raise TypeError(errmessage)

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for a in matrix:
        if type(a) is not list:
            raise TypeError(errmessage)
    MTX = []
    for row in matrix:
        MTX.append([round((a/div), 2) for a in row])
    return MTX
