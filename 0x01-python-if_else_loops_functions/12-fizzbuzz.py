#!/usr/bin/python3

def fizzbuzz():
    r = range(1, 101)
    for i in r:
        if i % 3 == 0 and i % 5 == 0:
            print("{}" .format("Fizz Buzz"), end=' ')
        elif i % 3 == 0:
            print("{}" .format("Fizz"), end=' ')
        elif i % 5 == 0:
            print("{}" .format("Buzz"), end=' ')
        else:
            print("{}" .format(i), end=' ')
