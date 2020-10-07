number1 = 15
number2 = 3
#pr_number = str(number)
print(number1)

action = input('Выберите арифметическое действие +, -, / или *: ')


if action == '+':
    print(str(number1 + number2))
if action == '-':
    print(str(number1 - number2))
if action == '/':
    print(str(number1 / number2))
if action == '*':
    print(str(number1 * number2))


