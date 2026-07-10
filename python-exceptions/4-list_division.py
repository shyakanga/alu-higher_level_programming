#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError
            val1 = my_list_1[i]
            val2 = my_list_2[i]
            if not isinstance(val1, (int, float)) or not isinstance(val2, (int, float)):
                raise TypeError
            result = val1 / val2
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            new_list.append(result)
    return new_list
