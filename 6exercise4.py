class Car:
    count = 0
    in_police = False

    def __init__(self, name, model, color, year, in_police):
        self.name = name
        self.model = model
        self.color = color
        self.year = year
        self.in_police = Car.in_police
        Car.count += 1




class TownCar(Car):
    count = 0

    def on_start(self, speed):
        print(f'Car {self.name} startinig with speed {speed}') if speed <= 60 else print(f'Car {self.name} startinig with speed {speed} km/h and crashed')

    def on_stop(self):
        print(f'Car {self.name} stoped')



class SportCar(Car):
    count = 0
    def on_start(self, speed):
        print(f'Car {self.name} startinig with speed {speed}') if speed <= 200 else print(f'Car {self.name} startinig with speed {speed} km/h and crashed')

    def on_stop(self):
        print(f'Car {self.name} stoped')


class WorkCar(Car):
    count = 0
    def on_start(self, speed):
        print(f'Car {self.name} startinig with speed {speed}') if speed <= 40 else print(f'Car {self.name} startinig with speed {speed} km/h and crashed')

    def on_stop(self):
        print(f'Car {self.name} stoped')


class PoliceCar(Car):
    count = 0
    def on_start(self, speed):
        print(f'Car {self.name} startinig with speed {speed}')


    def on_stop(self):
        print(f'Car {self.name} stoped')


car_1 = TownCar('ZAZ', '696', 'blue', 1996, False)
car_1.on_start(70)
car_1.on_stop()
car_2 = SportCar('lamborgini', 'diablo', 'red', 2006, False)
car_2.on_start(210)
car_3 = WorkCar('ZIL', '131', 'green', 2001, False)
car_3.on_start(70)
car_3.on_stop()
car_4 = PoliceCar('Shkoda', 'Octavia', 'white', 2019, True)
car_4.on_start(70)
car_4.on_stop()
