import threading
from threading import Thread
import time

class Knight(Thread):
    def __init__(self, name, power, enemies):
        threading.Thread.__init__(self)
        self.name = name
        self.enemies = enemies
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        day = 0
        while self.enemies > 0:
            self.enemies -= self.power
            time.sleep (1)
            day += 1
            print (f'{self.name} сражается {day}, осталось {self.enemies} врагов')
        print (f'{self.name} одержал победу спустя {day}дней(дня)')


knight1 = Knight('George Floyd', 10, 100)
knight2 = Knight('Lebron James', 5, 20)
knight1.start()
knight2.start()
knight1.join()
knight2.join()
