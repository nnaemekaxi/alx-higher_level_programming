#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        number = 0
        denom = 0
        for tupl in my_list:
            number += (tupl[0] * tupl[1])
            denom += tupl[1]
        return (number / denom)
    return 0
