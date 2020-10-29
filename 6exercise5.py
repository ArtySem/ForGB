class Stationary:
    title = None
    name = None

    def draw(self):
        print (self.name)

class Pen(Stationary):
   type_pen = {1: 'шариковая', 2: 'перьевая'}

   def __init__(self, name, type):
        self.name = name
        self.type = type
        print(f'{name} {Pen.type_pen.get(self.type)}')


class Pencil(Stationary):
    type_pencil = {1: 'простой', 2: 'цветной'}
    def __init__(self, name, type):
        self.name = name
        self.type = type
        print(f'{name} {Pencil.type_pencil.get(self.type)}')

class Handle(Stationary):
    color_handle = {1: 'красный', 2: 'желтый'}
    def __init__(self, name, color):
        self.name = name
        self.color = color
        print(f'{name} {Handle.color_handle.get(self.color)}')


obj_1 = Pen('Bic', 1)
obj_2 = Pencil('Конструктор', 2)






