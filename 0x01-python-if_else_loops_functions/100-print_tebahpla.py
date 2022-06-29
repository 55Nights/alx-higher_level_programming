#!/usr/bin/python3

x = range(97, 123)
for i in reversed(x):
    if i % 2 == 0:
        i = i
    else:
        i = i - 32
    print(chr(i), end='')
