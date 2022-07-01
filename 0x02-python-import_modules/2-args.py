#!/usr/bin/python3
import sys

if __name__ == "__main__":
    x = len(sys.argv) - 1
    if x == 0:
        print("{} arguments." .format(x))
    elif x == 1:
        print("{} argument:" .format(x))
    else:
        print("{} arguments:" .format(x))
    for z in range(1, x + 1):
        print("{}: {}" .format(z, sys.argv[z]))
