#!/usr/bin/python3
if __name__ == '__main__':

    import sys
    count = len(sys.argv)
    if count == 1:
        count = 0
        print("{} arguments.".format(count))
    if count > 1:
        print("{} arguments:".format(count-1))
        for c in range(1, count):
            print("{}: {}".format(c, sys.argv[c]))
