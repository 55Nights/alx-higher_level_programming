#!/usr/bin/python3
x = range(00, 100)
for i in x:
    if i == 99:
        print("{0:02}" .format(i))
    else:
        print("{0:02}" .format(i), end=', ')
