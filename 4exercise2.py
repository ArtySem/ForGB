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
for i in range(lenth_first):
    first_list.append(randint(1, 100))
print(first_list)
for i in range(1, lenth_first):
    if first_list[i] > first_list[i-1]:
        second_list.append(first_list[i])
print(second_list)


