my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
length = len(my_list)

index = 0
while index < length:
    print (my_list[index])
    index += 1

    if my_list[index] == 0:
        my_list.remove(0)
    elif my_list[index] < 0:
        break