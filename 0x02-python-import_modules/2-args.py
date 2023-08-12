#!/usr/bin/python3
if __name__ == '__main__':

    import sys
    count = len(sys.argv)
    if count == 1:
        print("{} arguments.".format(count-1))
    elif count == 2:
        count = count - 1
        print("{} argument.".format(count))
        print("{}: {}".format(count, sys.argv[count]))
    elif count > 2:
        print("{} arguments:".format(count-1))
        for c in range(1, count):
            print("{}: {}".format(c, sys.argv[c]))
