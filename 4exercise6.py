from itertools  import count, cycle

my_list = []
n = int(input('Какое число будет наименьшим в вашем списке? '))
m = int(input('Какое число будет набольшим в вашем списке? '))

for num in count(n, 1):
    if num < m:
        my_list.append(num)
    else:
        break
print(my_list)
m = 0
new_list = []
for num in cycle(my_list):
    if m <= 10:
        new_list.append(num)
        m += 1
    else:
        break
print(new_list)

