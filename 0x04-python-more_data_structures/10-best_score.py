#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict) is False:
        return None
    biggest = 0
    for i in a_dictionary.values():
        if i >= biggest:
            biggest = i
    for x, y in a_dictionary.items():
        if y == biggest:
            return x
