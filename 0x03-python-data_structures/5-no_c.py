#!/usr/bin/python3

def no_c(my_string):
    s = ""
    for i in my_string:
        if i == "c" or i == "C":
            pass
        else:
            s = s + i
    return s
