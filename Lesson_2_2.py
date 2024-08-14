first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first % second == 0 and first % third == 0:
    print (3)
elif first % second == 0 or first % third == 0:
    print (2)
else:
    print (0)