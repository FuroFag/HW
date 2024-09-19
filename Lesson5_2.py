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


h1 = House('ЖК Эльбрус', 30)
h2 = House('ЖК Приречный', 9)
print (len(h1))
print (str(h1))
print (len(h2))
print (str(h2))