my_list = input("введите через пробел произвольные числа в произвольном порядке: ").split()
print(my_list)
new_list = [num for num in my_list if my_list.count(num) == 1]
print('В нем не повторились: ', new_list)
