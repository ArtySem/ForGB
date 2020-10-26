my_subj = open('subejects.txt', 'r', encoding='UTF-8')
subjects = []
while True:
    current_string = my_subj.readline()
    if current_string != '':
        subjects.append(current_string)
    else:
        break
subjects_dict = {el.split(':')[0]: el.split(':')[1] for el in subjects}
for key in subjects_dict:
    elem = (''.join(i for i in subjects_dict.get(key) if i == ' ' or ('0' <= i <= '9'))).split()
    subjects_dict[key] = sum(map(int, elem))
print(subjects_dict)
my_subj.close()
