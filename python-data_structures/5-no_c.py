#!/usr/bin/python3
def no_c(my_string):
     characters = [l if l != "C" and l != "c" else "" for l in my_string]
     return "".join(characters)
 
