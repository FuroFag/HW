def is_prime(func):
    def wrapper(*args):
        summed = func(*args)
        if summed > 1:
            for i in range(2, (summed//2) + 1):
                if (summed % i) == 0:
                    return summed, 'Не простое'
                else:
                    return summed, 'Простое'
        else:
            return summed, 'Не простое'
    return wrapper

@is_prime
def sum_three(*args):
    _list = []
    for i in args:
        _list.append(i)
    result = sum(_list)
    return result

print(sum_three(1, 0, 11))
