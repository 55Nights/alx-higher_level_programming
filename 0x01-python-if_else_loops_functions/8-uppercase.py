#!/usr/bin/python3

def uppercase(str):
    for c in str:
        x = ord(c)
        if x >= 97 and x < 123:
            x -= 32
        print("{}" .format(chr(x)), end='')
    print("{}" .format('\n'))
