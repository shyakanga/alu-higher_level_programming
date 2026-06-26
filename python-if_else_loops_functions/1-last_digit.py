#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Snumber = str(number)
ls_digit = Snumber[-1]
if number < 0 and int(ls_digit) != 0:
    ls_digit = "-"+ls_digit
if int(ls_digit) > 5:
    ls_comp = "and is greater than 5"
elif int(ls_digit) == 0:
    ls_comp = "and is 0"
elif int(ls_digit) < 6 and int(ls_digit) != 0:
    ls_comp = "and is less than 6 and not 0"
print(f"Last digit of {number} is {ls_digit} {ls_comp}")
