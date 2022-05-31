#!/usr/bin/python3

def uppercase(str):
    for c in str:
        if (ord(c) <= 97 or ord(c) <= 122):
            c = chr(ord(c) - 32)
        print("{}".format(chr(c)), end="")
    print("")
