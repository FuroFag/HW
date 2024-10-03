class Vehicle:
    __COLOR_VARIANTS = ['Black', 'White', 'Red', 'Blue', 'Yellow', 'Gray', 'Purple', 'Green', 'DeepBlue']

    def __init__(self, owner:str, __model:str, __engine_power:int, __color:str,):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print (self.get_model())
        print (self.get_color())
        print (self.get_horsepower())

    def set_color(self, new_color):
        if new_color.upper() in map(str.upper, self.__COLOR_VARIANTS):
            self.__color = new_color
            print (f'цвет изменен на {new_color}')
        else:
            print (f'Невозможно выбрать "{new_color}" цвет')
class Sedan(Vehicle):
    __PASSANGERS_LIMIT = 5
    pass

toyota = Sedan('Владислав', 'Toyota RAF4', 240, 'deepblue')
toyota.print_info()
toyota.set_color('cyan')
toyota.set_color('yellow')
toyota.print_info()