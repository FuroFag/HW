def test_function():
    def inner_function():
        print ("Я в области видимости функции")
    b = inner_function()
    print (b)

a = test_function()
print (a)