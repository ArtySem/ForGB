def my_func(n):
    for el in range(1, n+1):
        yield el


n = int(input('Факториал какого числа будем искать?' ))
factorial = 1
for i in my_func(n):
    factorial = factorial * i

print(factorial)
