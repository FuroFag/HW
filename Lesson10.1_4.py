from queue import Queue
from threading import Thread
import time
import random
from time import sleep


class Table():
    def __init__(self, number):
        self.guest = None
        self.number = number
    
class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(random.randint(3, 10))

class Cafe():
    list_thr = []

    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)

    def guest_arrival(self, *guests):
        list_guests = list(guests)
        list_tables = self.tables
        guests_count = len(list_guests)
        min_guests_tables = min(guests_count, len(self.tables))
        for i in range(min_guests_tables):
            list_tables[i].guests = guests[i]
            thread1 = guests[i]
            thread1.start()
            Cafe.list_thr.append(thread1)
            print(f'{list_guests[i].name} сел(-а) за стол номер {list_tables[i].number}')
        if guests_count > min_guests_tables:
            for i in range(min_guests_tables, guests_count):
                self.queue.put(guests[i])
                print(f'{list_guests[i].name} в очереди')
    
    def discuss_guests(self):
        while not (self.queue.empty()) or Cafe.check_table(self):
            for table in self.tables:
                if not (table.guest is None) and not (table.guest.is_alive()):
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if (not (self.queue.empty())) and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    thread1 = table.guest
                    thread1.start()
                    Cafe.list_thr.append(thread1)
    
    def check_table(self):
        for table in self.tables:
            if table.guest is not None:
                return True
        return False

tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
# cafe.guest_arrival(*guests)
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
for thr in Cafe.list_thr:
    thr.join()