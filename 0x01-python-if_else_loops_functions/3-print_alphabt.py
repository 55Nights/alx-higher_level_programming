#!/usr/bin/python3
r = range(97, 123)
for i in r:
    if i != 101 and i != 113:
        print("{}" .format(chr(i)), end='')
