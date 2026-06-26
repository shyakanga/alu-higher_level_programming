#!/usr/bin/python3
import random
number = random.randint(-10, 10)
result = (
    "is positive" if number > 0 else
    "is negative" if number < 0 else
    "is zero"
)
print(f"{number} {result}")
