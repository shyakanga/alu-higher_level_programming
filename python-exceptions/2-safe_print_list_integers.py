#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nb_print = 0
    try:
        for i in range(x):
            val = my_list[i]
            if isinstance(val, int) and not isinstance(val, bool):
                print("{:d}".format(val), end="")
                nb_print += 1
    except ValueError:
        pass
    print()
    return nb_print
