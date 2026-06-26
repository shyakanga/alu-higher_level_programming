#!/usr/bin/python3
for l in range(97, 123):
    if f"{l:c}" == "q" or f"{l:c}" == "e":
        continue
    print("{:c}".format(l), end="")
