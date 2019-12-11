#!/usr/bin/python3
def uppercase(str):
    string = 0
    for upper in str:
        if ord(upper) >= ord('a') and ord(upper) <= ord('z'):
            string = 32
        else:
            string = 0
        print("{:c}".format(ord(upper) - string), end='')
    print()
