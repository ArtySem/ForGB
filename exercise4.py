number_user = int(input("C каким числом будем работать? "))
max_figure = 0
while number_user >= 1:
    if max_figure < number_user % 10:
       max_figure = number_user % 10
    number_user = number_user // 10
print(f'Наибольшая цифра в нашем числе = {max_figure}')
