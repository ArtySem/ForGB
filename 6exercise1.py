import time


class TrafficLight:
    color = 'red'


    def running(self):
        print(f'\r{self}', end='')

x = None
t = TrafficLight
while True:
    t.running('red')
    time.sleep(7)
    t.running('yellow')
    time.sleep(2)
    t.running('green')
    time.sleep(7)
    t.running('yellow')
    time.sleep(2)



