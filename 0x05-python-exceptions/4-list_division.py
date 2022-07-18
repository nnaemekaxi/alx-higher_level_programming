#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for a in range(0, list_length):
        try:
            divi_elmnt = my_list_1[a] / my_list_2[a]
        except TypeError:
            print("wrong type")
            divi_elmnt = 0
        except ZeroDivisionError:
            print("division by 0")
            divi_elmnt = 0
        except IndexError:
            print("out of range")
            divi_elmnt = 0
        finally:
            new_list.append(divi_elmnt)
    return (new_list)
