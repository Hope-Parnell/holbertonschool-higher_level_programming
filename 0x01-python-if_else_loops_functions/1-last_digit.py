#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % -10 if number < 0 else number % 10
print("Last digit of {} is {} and is {}"
      .format(number, lastDigit,
              "greater than 5" if lastDigit > 5
              else "0" if lastDigit == 0
              else "less than 6 and not 0"))
