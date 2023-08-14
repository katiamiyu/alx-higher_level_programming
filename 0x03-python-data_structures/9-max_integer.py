#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    else:
        point = 0
        end = len(my_list)
        while point < end:
            point_2 = end - 1
            while point_2 > point:
                if my_list[point_2] < my_list[point]:
                    temp = my_list[point_2]
                    my_list[point_2] = my_list[point]
                    my_list[point] = temp
                point_2 -= 1
            point += 1
        return my_list[end - 1]
