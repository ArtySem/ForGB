time_user = int(input('Введите время в секундах'))

time_hour = str(time_user // 3600)
time_user = time_user % 3600
time_minutes = str (time_user // 60)
time_user = str(time_user % 60)

print(time_hour, time_minutes, time_user, sep=":")