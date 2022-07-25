#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        n = 0
        y = 0
        while n < x:
            if isinstance(my_list[n], int) is True:
                print("{:d}".format(my_list[n]), end='')
                y = y + 1
            else:
                pass
            n = n + 1
        print()
    except IndexError:
        print("list index out of range")
    else:
        return y
