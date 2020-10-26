from random import randint
my_numbers = open('numbers1.txt', 'w', encoding='UTF-8')
numbers = [str(randint(0, 9)) for _ in range(20)]
my_numbers.write(' '.join(numbers))
my_numbers.close()
my_numbers = open('numbers1.txt', 'r', encoding='UTF-8')
numbers1 = my_numbers.read().split()
print(numbers1)
summ = 0
for el in numbers1:
    summ += int(el)
print(summ)
