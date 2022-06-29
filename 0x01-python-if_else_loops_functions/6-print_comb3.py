#!/usr/bin/python3
x = range(0, 10)
for i in x:
    for j in range(i + 1, 10):
        if x == 8 and j == 9:
            print("{}{}" .format(i, j))
        else:
            print("{}{}" .format(i, j), end=', ')
