#!/usr/bin/python3
def print_last_digit(number):
    newnumber = abs(number) % 10
    print("{}".format(newnumber), end="")
    return newnumber
