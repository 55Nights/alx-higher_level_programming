#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    num = len(sys.argv) - 1

    if num != 3:
        print("{}" .format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    o = str(sys.argv[2])

    if o == "+":
        print("{} {} {} = {}" .format(a, o, b, add(a, b)))
    elif o == "-":
        print("{} {} {} = {}" .format(a, o, b, sub(a, b)))
    elif o == "*":
        print("{} {} {} = {}" .format(a, o, b, mul(a, b)))
    elif o == "/":
        print("{} {} {} = {}" .format(a, o, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
