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
        if isinstance (other, House):
            return self.nof < other.nof
        elif isinstance(other, int):
            return self.nof < other

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __gt__(self, other):
        return not self.__lt__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, value:int):
        if isinstance (value, int):
            self.nof += value
            return self
        if isinstance(value, House):
            self.nof += other.nof
        return self

    def __radd__(self, other:int):
        return  self.__add__(other)

    def __iadd__(self, other:int):
        return self.__add__(other)

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