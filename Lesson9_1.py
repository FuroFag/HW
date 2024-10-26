def apply_all_func(int_list, *function):
    results = {}
    for funcs in function:
        results[funcs.__name__] = funcs(int_list)
    return results

print (apply_all_func([1,2,3,4,5,6,7], len, min, sum))
print (apply_all_func([100, 21, 31, 84, 999], max, min, sorted))