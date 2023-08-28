#1/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    int i = 0
    while i < x:
        try:
            print(mylist[i], end='')
        except IndexError:
            break
    i++;

print("")
return (i);
