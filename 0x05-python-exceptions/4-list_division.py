#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    i = 0
    res = []
    ans = 0
    while (i < list_length):
        try:
            ans = my_list_1[i] / my_list_2[i]
        except (IndexError):
            print("out of range")
            ans = 0
        except (TypeError):
            print("wrong type")
            ans = 0
        except (ZeroDivisionError):
            print("division by 0")
            ans = 0
        finally:
            res.append(ans)
        i = i + 1
    return res
