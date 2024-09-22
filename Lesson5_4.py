class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self ,name, nof):
        self.name = name
        self.nof = nof

    def __del__(self):
        print(f'{self.name}, удален, но он остался в истории')

    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if 1 <= new_floor <= self.nof:
                print(i)
            else:
                print('Такого этажа нет')
                break

    def __len__(self):
        return self.nof

    def __str__(self):
        return (f'{self.name} {self.nof}')

    def __eq__(self, other):
        if self.nof == other.nof:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.nof < other.nof:
            return True
        else:
            return False

    def __le__(self, other):
        if self.nof <= other.nof:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.nof > other.nof:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.nof >= other.nof:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.nof != other.nof:
            return True
        else:
            return False

    def __add__(self, value):
        self.nof = self.nof + value
        return self.nof

    def __radd__(self, value):
        self.nof = self.nof + value
        return self.nof

    def __iadd__(self, value):
        self.nof = self.nof + value
        return self.nof


h1 = House('ЖК Эльбрус', 30)
print(h1.houses_history)
h2 = House('ЖК Приречный', 9)
print (h2.houses_history)

del h2
print (House.houses_history)
