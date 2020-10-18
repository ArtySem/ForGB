from random import random, randint
first_list = []
second_list = []
while True:
    lenth_first = input('Какую длину списка вы хотите? ')
    try:
        int(lenth_first)
    except ValueError:
        continue
    else:
        lenth_first = int(lenth_first)
        break
first_list = [randint(1, 100) for i in range(lenth_first)]

print(first_list)

second_list = [(first_list[i])for i in range(1, lenth_first) if first_list[i] > first_list[i-1]]

print(second_list)


