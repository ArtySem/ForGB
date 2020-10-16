def my_func(a, b):
    if b == 0:
        return 1
    else:
        l = 1
        for i in range(0, abs(b)):
            l = l * a
        if b > 0:
            return l
        else:
            return 1/l


print('Данная программа возводит в степень')
while True:
    user_number = input('Введите число возводимое в степень: ')
    exp_number = input('Введите требуемую степень: ')
    try:
        float(user_number)
        int(exp_number)
    except ValueError:
        print(user_number + '^' + exp_number)
        continue
    else:
        break

user_number = float(user_number)
exp_number = int(exp_number)

print(f'Результат деления равен {my_func(user_number, exp_number):.03f}')
