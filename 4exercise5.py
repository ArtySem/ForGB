from functools import reduce


def my_func(var_1, var_2):
    return var_1 * var_2


my_list = [num for num in range(100, 1001, 2)]

print(reduce(my_func, my_list))
