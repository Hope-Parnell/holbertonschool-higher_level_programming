#!/usr/bin/python3
"""Module creates a new matrix by dividing each item in
a matrix by a specific number
"""


def matrix_divided(matrix, div):
    """This function creates a new matrix by dividing matrix by div

    Args:
        matrix(object): the matrix to divide
        div(int/float): number to divide by
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    matrix_error = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list:
        raise TypeError(matrix_error)

    row_error = "Each row of the matrix must have the same size"

    for row in matrix:
        if type(row) is not list:
            raise TypeError(matrix_error)
        if len(row) != len(matrix[0]):
            raise TypeError(row_error)
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError(matrix_error)

    new_matrix = new_matrix = list(map(list, matrix))
    for row in range(len(new_matrix)):
        for x in range(len(new_matrix[row])):
            new_matrix[row][x] = round((matrix[row][x] / div), 2)

    return new_matrix
