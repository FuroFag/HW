from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop(Product):

    def __init__(self, name, weight, category, __file_name = 'products.txt'):
        super().__init__(name, weight, category)
        self.__file_name = __file_name

    def get_products(self):
        file = open(self.__file_name, 'r')
        a = file.read()
        file.close()
        print (f'{a}')

    def add(self, *products):
        for i in products:
            new = str(i)
            file = open(self.__file_name, 'r')
            f = file.read()
            file.close()
            if new in f:
                print (f'продукт {new} уже существует')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'\n{new}')
                file.close()

shop = Shop('', 0, '')
p1 = Product('Fumo', 200, 'funny stuff')
p2 = Product('mini figures', 50, 'collectable stuff')

shop.add(p1, p2)
shop.get_products()