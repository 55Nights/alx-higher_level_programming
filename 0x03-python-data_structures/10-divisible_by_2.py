#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    listA = []
    for i in my_list:
        if i % 2 == 0:
            listA.append(True)
        else:
            listA.append(False)

    return listA
