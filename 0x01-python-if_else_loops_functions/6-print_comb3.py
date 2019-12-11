#!/usr/bin/python3
for number_a in range(0, 9):
    for number_b in range(number_a + 1, 10):
        print("{}".format(number_a), end='')
        if number_a == 8 and number_b == 9:
            print("9", end='\n')
        else:
            print("{}".format(number_b), end=', ')
