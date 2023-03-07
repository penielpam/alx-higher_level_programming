#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print('{} is positive'.Format(number))
elif number == 0:
    print('{} is zero'Format(number))
else:
    print('{} is negative'.Format(number))
