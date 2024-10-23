def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i

        except TypeError as exc:
            incorrect_data += 1
            print(f'Неправильный тип данных - {i}. '
                f'Кол-во данных неправильного типа {incorrect_data}')
    return result, incorrect_data

def calculate_avrg(numbers):
    try:
        _sum = personal_sum(numbers)
        return _sum[0]/(len(numbers) - _sum[1])
    except ZeroDivisionError as exc:
        return 0
    except TypeError as exc:
        return print (f'Указан некорректный тип данных')

print (calculate_avrg([1, 15, 36, 13]))