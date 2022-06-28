#!/usr/bin/python3
x = range(0, 100)
for i in x:
    if i < 10 and i != 99:
        print("0{:d}" .format(i), end=', ')
    elif i != 99:
        print("{:d}" .format(i), end=', ')
    else:
        print("{:d}" .format(i))
