first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
a = ()
result1 = [len(x) for x in first_strings if len(x) >= 5]

result2 = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
full_string = first_strings + second_strings
result3 = [{x: len(x)} for x in full_string if len(x) %2 == 0]

print (result1)
print (result2)
print (result3)