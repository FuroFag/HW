class House:
    def __init__(self ,name, nof):
        self.name = name
        self.nof = nof

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
        if isinstance (other, int):
            return self.nof == other.nof

    def __lt__(self, other):
        if isinstance (other, int):
            return self.nof < self.other

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

    def __add__(self, value:int):
        if isinstance (value, int):
            self.nof += value
            return self

    def __radd__(self, value:int):
        return  self.__add__

    def __iadd__(self, value:int):
        return self.__add__

h1 = House('ЖК Эльбрус', 30)
h2 = House('ЖК Приречный', 9)
print (len(h1))
print (str(h1))
print (len(h2))
print (str(h2))
print (h1 == h2)
print (h1 < h2)
print (h1 <= h2)
print (h1 > h2)
print (h1 >= h2)
print (h1 != h2)
h1 = h1 + 11
print (h1)
h2 = h2 + 2
print (h2)
h1 = 1 + h1
print (h1)