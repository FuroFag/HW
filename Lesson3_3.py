def print_params(a = 1, b = 'string', c = True):
    print (a, b, c)

print_params(b = 25, c = [1, 2, 3])
print_params(a = False)
print_params()

values_list = [1, 'not a string', True]
dict_ = {'a': 12, 'b': 'integer', 'c': True}
print_params(*values_list)
print_params(**dict_)

values_list2 = [22, True] #если values_list так хорош то где values_list2 
print_params(*values_list2)