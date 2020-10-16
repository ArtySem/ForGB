def ver_func(x):
    try:
        float(x)
    except ValueError:
        return x
    else:
        return float(x)

summ = 0
while True:
    any_list = input('Введите любые числа через пробел, если хотите выйти наберите q ').split()
    for element in any_list:
        if type(ver_func(element)) == float:
            summ += ver_func(element)
        else:
            print(summ)
            spec_symbol = element
            break
    if spec_symbol == 'q' or spec_symbol == 'Q':
        break
print('Ok')






