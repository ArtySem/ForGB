my_numbers = open('numbers.txt', mode='r', encoding='UTF-8')
out_numbers = open('outnum.txt', mode='w', encoding='UTF-8')
out_numbers.write('')
out_numbers.close()
out_numbers = open('outnum.txt', mode='a', encoding='UTF-8')
rus_dyct = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре'}
list_numbers = my_numbers.read().split('\n')
numbers = {el.split(' - ')[0]: el.split(' - ')[1] for el in list_numbers if el != ''}
for key in numbers.keys():
    out_numbers.write(f'{rus_dyct.get(key)} - {numbers.get(key)}\n')
    print(f'{rus_dyct.get(key)} - {numbers.get(key)}\n')
print(numbers)
my_numbers.close()
out_numbers.close()
