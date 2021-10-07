#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        print("{}".format("FizzBuzz" if x % 5 == 0 and x % 3 == 0
                          else "Fizz" if x % 3 == 0
                          else "Buzz" if x % 5 == 0
                          else x), end=" ")
