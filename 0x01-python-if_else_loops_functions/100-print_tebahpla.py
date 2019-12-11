#!/usr/bin/python3
for alpha in range(122, 96, -1):
    if alpha % 2 != 0:
        print('{}'.format(chr(alpha - 32)), end='')
    elif alpha % 2 == 0:
        print('{}'.format(chr(alpha)), end='')
