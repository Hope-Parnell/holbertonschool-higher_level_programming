#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for L in my_string:
        if L != 'c' and L != 'C':
            new_string += L
    return new_string
