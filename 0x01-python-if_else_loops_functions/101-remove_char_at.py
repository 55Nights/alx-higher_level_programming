#!/usr/bin/python3
def remove_char_at(str, n):
    if n > len(str) or n < 0:
        return str
    else:
        ch = ''
        c = str[n]
        for i in str:
            if i != c:
                ch = ch + i

    return (ch)
