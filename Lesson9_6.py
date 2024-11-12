from itertools import combinations

def all_variants(text):
    _list = []
    for i in range(1, len(text)+1):
        _list = []
        comb = combinations(text, i)
        _list.extend(comb)
        for j in _list:
            j = list(j)
            yield(''.join(j))

first_test = all_variants('abc')
for i in first_test:
    print (i)

second_test = all_variants('123456789')
for j in second_test:
    print(j)