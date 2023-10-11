#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    resma = []

    for row in matrix:

        result_row = []

        for value in row:
            result_row.append(value ** 2)

        resma.append(result_row)

    return resma
