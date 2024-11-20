import threading
from threading import Thread, Lock
import time
import random

class Bank(Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.Locked():
                self.lock.release()
            a = random.randint(50, 500)
            self.balance += a
            print (f'Пополнение: {a}. Баланс: {self.balance}')
            time.sleep(0.001)
    
    def take(self):
        for i in range(100):
            b = random.randint(50,500)
            print(f'Запрос на {b}')
            if self.balance >= b:
                self.balance -= b
                print(f'Снятие: {b}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)

test = Bank()

obj1 = threading.Thread(target=Bank.deposit, args=(test,))
obj2 = threading.Thread(target=Bank.take, args=(test,))

obj1.start()
obj2.start()
obj1.join()
obj2.join()

print (f'Итоговый баланс: {test.balance}')