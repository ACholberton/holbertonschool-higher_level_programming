#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for i in matrix:
        for a in matrix:
            return[[a ** 2 for a in i]for i in matrix]
