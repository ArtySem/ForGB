my_list = [7, 5, 3, 3, 2]
print(my_list)
while True:
    user_number = input('Введите любое число от 1 до 9')
    if len(user_number) > 1 or int(user_number) == 0:
        continue
    else:
        break
for i in range(0, len(my_list)):
    if int(user_number) > my_list[i]:
        my_list.insert(i, int(user_number))
        break
if int(user_number) not in my_list:
    my_list.append(int(user_number))
print(my_list)
