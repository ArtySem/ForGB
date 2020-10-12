my_list = []
lenth_list = int(input('Какую длину списка будем использовать: '))
i = 1
while i <= lenth_list:
    user_number = int(input(f'Введите {i} число массива: '))
    my_list. append(user_number)
    i += 1
print(my_list)
i = 0
while i + 2 <= len(my_list):
    my_list.insert(i, my_list[i+1])
    my_list.pop(i+2)
    i += 2
print(my_list)
