#!/usr/bin/python3
import sys
argv = sys.argv
n = len(argv) - 1
if n == 0:
    print("0 arguments.")
elif n == 1:
    print("1 argument:")
else:
    print("{:d} arguments:".format(n))
for i in range(1, len(argv)):
    print("{:d}: {:s}".format(i, argv[i]))
