profit_company = int(input('Выручка вашей компании составила: '))
costs_company = int(input('Издержки вашей компании составили: '))
rent_company = profit_company / costs_company
if profit_company > costs_company:
    print ('Ваша компания прибыльна')
else:
    print('Ваша компания убыточна')
print(f'Рентабельность вашей компании составила {rent_company}')
personal_company = int(input('Сколько людей у вас работает? '))
print(f'Каждый работкник вашей компании заработал, в среднем, {profit_company/personal_company}')
