#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
new_list = new_in_list(my_list, 0, new_element)
print(new_list)
print(my_list)
new_list = new_in_list(my_list, -7, new_element)
print(new_list)
print(my_list)
my_list[3] = 149
print(new_list)
print(my_list)
new_list[0] = 7
print(new_list)
print(my_list)
new_list = new_in_list(my_list, 5, new_element)
print(new_list)
print(my_list)
