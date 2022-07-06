#!/usr/bin/python3
def roman_to_int(roman_string):
    nums_dict = {'M': 1000, 'D': 500, 'C': 100,
                 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    a = 0
    total = 0
    if isinstance(roman_string, str):
        for a in range(len(roman_string) - 1):
            if nums_dict[roman_string[a]] >= nums_dict[roman_string[a + 1]]:
                total += nums_dict[roman_string[a]]
            else:
                total -= nums_dict[roman_string[a]]
            a += 1
        total += nums_dict[roman_string[a]]
        return total
    else:
        return 0
