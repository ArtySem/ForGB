import sys, time

x = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
print(x)
file_x = open('result.txt', 'w', encoding='UTF-8')
file_x.write(f'Запись от {x} \n')
file_x.close()
file_x = open('result.txt', 'a', encoding='UTF-8')
while True:
    user_string = input('Введите что-нибудь, а мы запишем в файл')
    if user_string == '':
        break
    else:
        file_x.write(user_string + '\n')
print('Ваши записи добавлены в файл')
file_x.close()
