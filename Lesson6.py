my_dict = {'Glep': 1989, 'Nill': 1999}
print ('существующее значение:', my_dict ['Glep'])
print ('несуществующее значение:', my_dict.get('Jack'))
my_dict['Lisa'] = 1964
my_dict['Mark'] = 2000
a = my_dict.pop('Mark')
print ('Удаленное значение', a)
print (my_dict)

#множества

my_set = {'the "True" is not a boolean', 112, 221, 222, 111,'integer', True, 112, 221, 110}
print(my_set)
my_set.add(999)
my_set.add('999 will be deleted and you will not know')
my_set.remove(999)
print (my_set)