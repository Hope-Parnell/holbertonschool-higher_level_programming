#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False or roman_string is None:
        return 0
    rtoi = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    total = 0
    for i in range(len(roman_string)):
        a = roman_string[i]
        if (i + 1) != len(roman_string):
            b = roman_string[i + 1]
        else:
            b = None
        if b is not None and rtoi[a] < rtoi[b]:
            i += 1
            total += rtoi[b] - rtoi[a]
        else:
            total += rtoi[a]
    return total
