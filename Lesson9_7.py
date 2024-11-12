def is_prime(func):
    def wrapper(*args):
        summed = func(*args)
        prime = True
        if summed > 1:
            for i in range(2, (summed//2) + 1):
                if (summed % i) == 0:
                    prime = False
                    break
            if prime == True:
                return f'{summed} Простое'
            else:
                return f'{summed} Не простое'
        else:
            return f'{summed} Простое'
    return wrapper

@is_prime
def sum_three(*args):
    _list = []
    for i in args:
        _list.append(i)
    result = sum(_list)
    return result

print(sum_three(1, 0, 10))
