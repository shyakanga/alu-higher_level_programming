#!/usr/bin/python3
import hidden_4
for name in dir(hidden_4):
    if name[:2] != "__":
        print(name)
