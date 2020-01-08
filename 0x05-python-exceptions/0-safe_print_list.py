#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    numbers = 0
    for element in range(x):
        try:
            print(my_list[element], end="")
            numbers += 1
        except:
            break
    print()
    return numbers
