#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    n = 0
    while (i < x):
        try:
            print("{:d}".format(my_list[i]), end="")
            n += 1
        except (ValueError, TypeError):
            pass
        except IndexError:
            break
        i += 1
    print("")
    return (n)
