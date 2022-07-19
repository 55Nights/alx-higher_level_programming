#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        y = a / b
        return y
    except BaseException:
        y = None
        return y
    finally:
        print("Inside result: {}".format(y))
