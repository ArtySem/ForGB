class Worker():
    count = 0



class position(Worker):
    __incom = {'vage': 9000, 'bonus': 5500}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        #self.income = position.income
        print(f'{self.surname} {self.name} {self.position}')

    def get_full_name(self):
        return f'{self.surname} {self.name}'


    def get_total_income (self):
        total_incom = position.__incom.get('vage') + position.__incom.get('bonus')
        return f"total_incom = {total_incom}"




p_1 = position('Ivan', 'Petrov', 'manager')
print(p_1.get_full_name())
print(p_1.get_total_income())
print(p_1._position__incom)






