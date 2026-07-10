#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_chr = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    chara = [roman_chr.get(l, 0) for l in roman_string]
    total = 0
    length = len(chara)
    for i in range(length):
        if i + 1 < length and chara[i] < chara[i + 1]:
            total -= chara[i]
        else:
            total += chara[i]
    return total
