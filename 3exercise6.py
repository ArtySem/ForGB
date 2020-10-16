def int_func(word):
    n = 0
    for letter in word:
        if ord(letter) in range(97, 123):
            n += 1
    if n == len(word):
        return word
    else:
        return None


out_string = []
my_string = input('Введите несколько слов через пробел: ').split()
for word in my_string:
    if int_func(word) is not None:
        out_string.append(word.title())
print(' '.join(out_string))
