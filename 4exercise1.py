from sys import argv

print(argv)
name, time_work, payment_h, bonus = argv
time_work = int(time_work)
payment_h = int(payment_h)
bonus = int(bonus)
if int(time_work) >= 60:
    payment = time_work * payment_h + bonus
else:
    payment = time_work * payment_h
print (f'Ваша зарплата в этом месяце составила: {payment}')
