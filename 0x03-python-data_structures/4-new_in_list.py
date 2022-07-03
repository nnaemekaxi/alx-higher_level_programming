#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    #  function that replaces an element in a list
    new_list = my_list[:]
    if 0 <= idx < len(new_list):
        new_list[idx] = element
        return (new_list)
    return (my_list)
