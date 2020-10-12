my_list = []
words_user = input('введите, то что вам взбредет в голову: ')

my_list = words_user.split()
for i in range(0, len(my_list)):
    current_word = my_list[i]
    if len(current_word) > 10:
        current_word = current_word[0:11]
        print(f'{i+1}. {current_word}...')
    else:
        print(f'{i+1}. {current_word}')

