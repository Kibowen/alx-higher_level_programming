#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# convert integer to string
string = str(number)

# stores the last digit
num_last = string[-1:]

# checks the conditions provided.
if num_last > "5":
    print("Last digit of", number, "is", num_last, "and is greater than 5")
elif num_last == "0":
    print("Last digit of", number, "is", num_last, "and is 0")
elif num_last < "6":
    print("Last digit of", number, "is", num_last, "and is less than 6 and not 0")
