
my_workers = open('personal.txt', mode='r', encoding='UTF-8')
list_workers = my_workers.read().split('\n')
workers = [el.split() for el in list_workers if el != '']
w = {el[0]: float(el[1]) for el in workers}
average_payment = sum(w.values()) / len(w)
print(w)
print(average_payment)
great_workers = [key for key, value in w.items() if value > 20000]
print(great_workers)
my_workers.close()
