def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        line = [value]*m
        matrix.append(line)
    return matrix


result = get_matrix(int(input()), int(input()), int(input()))
print (result)
