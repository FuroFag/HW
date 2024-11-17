import threading
from threading import Thread
import time

class Knight(Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self, enemies):
        print(f'{self.name}, на нас напали!')
        day = 0
        while enemies > 0:
            enemies -= self.power
            time.sleep (1)
            day += 1
            print (f'{self.name} сражается {day}, осталось {enemies} врагов')
        print (f'{self.name} одержал победу спустя {day}дней(дня)')


knight1 = Knight('George Floyd', 10)
knight1.run(110)
knight2 = Knight('Lebron James', 5)
knight2.run(25)
knight1.start()
knight2.start()

