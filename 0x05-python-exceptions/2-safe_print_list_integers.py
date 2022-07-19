#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        i = 0;
        while i < x:
            y = my_list[i]
            if type(y) ==  type(int):
                print("{:d}".format(y),end='')
            else:
                pass
            i += 1
        print()
        return x
    except IndexError:
        print("list index out of range")
        y = 0
        for x in my_list:
            y += 1
        return y

