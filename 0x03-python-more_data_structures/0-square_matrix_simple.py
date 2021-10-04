#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list(map(list, matrix))
    for row in range(len(new_matrix)):
        for x in range(len(new_matrix[row])):
            new_matrix[row][x] = matrix[row][x] * matrix[row][x]
    return new_matrix
