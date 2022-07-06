#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def search_replace(element):
        return (element if element != search else replace)
    return list(map(search_replace, my_list))
