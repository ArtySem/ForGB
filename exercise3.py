#Запрашиваем число n, с которым будем производить вычисления
number_user = int(input("Над каким числом вам хотелось бы поиздеваться? "))
#Обнуляем счетчики циклов
i = 0
j = 0
#Обнуляем переменные промежуточных величин
result_mult = 0 #Промежуточная величина, образующаяся при сдвиге
result_summ = 0 #Промежуточная величина, образующаяся при суммировании

k = number_user
bit_number = 1
# Определение количества разрядов в числе n
while k // 10 >= 1:
    k = k // 10
    bit_number += 1
print(f'Разрядность числа {str(bit_number)}')

while j <= 2:
    #Цикл вычисления текущего члена суммы (n, nn, nnn)
    while i <= j:
        result_mult = number_user + result_mult * (10 ** bit_number)
        i += 1
    result_summ = result_summ + result_mult
    j += 1
print(str(result_summ))