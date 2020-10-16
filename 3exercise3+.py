def adder_max(x, y, z):
    my_sum = x + y + z
    return my_sum - min(x, y, z)

my_list = input('Введите любые 3 числа через пробел ').split()
for i in range(0, len(my_list)):
    my_list[i] = float(my_list[i])

print(adder_max(my_list[0], my_list[1], my_list[2]))
