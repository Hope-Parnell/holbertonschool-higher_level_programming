#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) == 0:
        print("")
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            print("{}".format(matrix[x][y]),
                  end=" " if y < len(matrix[x]) - 1 else "\n")
