#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_Dic = {}
    for k, v in a_dictionary.items():
        new_Dic[k] = v * 2
    return new_Dic
