my_file = open('inner.txt', 'r', encoding='UTF-8')
read_res = my_file.read()
strings_file = read_res.split('\n')
number_strings = len(strings_file)
print(f'В файле {number_strings} строк')
word_string = [len(el.split()) for el in strings_file]
for i in range(len(word_string)):
    print(f'Cлов в {i + 1}-й строке {word_string[i]}')
my_file.close()