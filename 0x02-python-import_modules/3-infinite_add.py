#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sum = 0
    for i in range(1, len(sys.argv)):
        y = sys.argv[i]
        z = int(y)
        sum = sum + z
    print("{}" .format(sum))
