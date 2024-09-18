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

h1 = House('ЖК Эльбрус', 30)
h1.go_to(5)
h2 = House('ЖК Приречный', 9)
h2.go_to(101)