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
        y = sys.argv
        z = 1
        while z <= x:
            print("{}: {}" .format(z, y[z]))
            z += 1
