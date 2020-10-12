print('Операции со списком')
my_list = [1, 3.2, [7, 2], 'A', {18, 1}]
print(type(my_list))
print(my_list)
my_list.append(9)
print(my_list)
my_list.append(9)
print(my_list[0])


for i in range(0, len(my_list)):
    if type(my_list[i]) == int:
        print(f'{my_list[i]} - целое число')
    if type(my_list[i]) == float:
        print(f'{my_list[i]} - число с плавающей запятой')
    if type(my_list[i]) == str:
        print(f'{my_list[i]} - данные строкового типа')
    if type(my_list[i]) == list:
        print(f'{my_list[i]} - список')
    if type(my_list[i]) == set:
        print(f'{my_list[i]} - множество')
number_user = input('введите число')
my_list.append(number_user)
print(my_list)
#print('Операции с множеством')
#my_set = {1, 3, 2, 7}
#print(type(my_set))
#print(my_set)

#print('Операции с кортежем')
#my_tuple = (1, 3, 2, 7)
#print(type(my_tuple))
#print(my_tuple)

