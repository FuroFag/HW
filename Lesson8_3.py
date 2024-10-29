class InvalidVinType(Exception):
    def __init__(self, message):
        print (message)

class InvalidNumbers(Exception):
    def __init__(self, message):
        print(message)

class Car():
    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    def __is_valid_vin(self, vin):
        if not isinstance(vin, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not (1000000 <= vin <= 9999999):
            raise InvalidVinType('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise InvalidNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise InvalidNumbers('Неверная длина номера')
        return True


car = Car('седан', 2331421, '711833')
print (car)