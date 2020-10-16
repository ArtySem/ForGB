def my_func(**kwargs):
    return kwargs

user_name = input('введите ваше имя: ')
user_firstname = input('введите вашу фамилию: ')
user_birthyear = input('в каком году вы родились: ')
user_city = input('в каком городы вы проживаете: ')
user_email = input('адрес вашей электронной почты: ')
user_phone = input('ваш телефонный номер: ')
my_dict = my_func(name=user_name, firstname=user_firstname, birthyear=user_birthyear, city=user_city, email=user_email,
                  phone=user_phone)
print(f"{my_dict['firstname']} {my_dict['name']} {my_dict['birthyear']} года рождения проживает в городе {my_dict['city']}, "
      f"e-mail:  {my_dict['email']}, конт.тел. {my_dict['phone']}. ")


