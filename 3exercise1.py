def my_func(a, b):
    result_div = a / b
    return result_div

print('Данная программа выполняет деление')
while True:
    dividend_number = input('Введите делимое: ')
    divider_number = input('Введите делитель: ')
    try:
        float(dividend_number)
        float(divider_number)
    except ValueError:
        print(dividend_number + '/' + divider_number)
        continue
    else:
        break

dividend_number = float(dividend_number)
divider_number = float(divider_number)

print(dividend_number)
print(divider_number)
if divider_number != 0:
    print(f'Результат деления равен {my_func(dividend_number, divider_number):.03f}')
else:
    print('Результат деления бесконечен')


