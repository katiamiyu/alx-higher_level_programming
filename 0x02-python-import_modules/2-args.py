#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    count = len(argv)
    if count == 1:
        print("{:d} arguments.".format(count - 1))
    elif count == 2:
        print("{:d} arguments.".format(count - 1))
        print("{:d}: {}".format(n - 1, argv[1]))
    else:
        print("{:d} arguments.".format(n - 1))
        for val in range(1, count):
            print("{:d}: {}".format(val, argv[val]))
