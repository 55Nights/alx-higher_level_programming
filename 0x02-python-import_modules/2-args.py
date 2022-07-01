#!/usr/bin/python3
import sys
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
