#1/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    int i = 0
    try:
        while i < x:
            print(mylist[i], end='')
            i++;
    except IndexError:
        pass

print("")
return (i);
