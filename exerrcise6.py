lenrun_begin = int(input('Сколько километров вы пробегаете в день? '))
lenrun_target = int(input('Сколько километров вы хотели бы пробегать в день? '))
lenrun_delta = 0.6
lenrun_current = lenrun_begin
count = 1
while lenrun_current < lenrun_target:
    lenrun_current = lenrun_current * 1.1
    count += 1

print(f'Чтобы вы смогли пробежать более {lenrun_target} километров, вам нужно тренироваться не менее {count} дней')