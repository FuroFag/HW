import inspect
from pprint import pprint

class ClassTest():
    def __init__(self):
        a = 1

    def testfunc(b):
        pass

testobj = ClassTest()

def introspection_info(arg):
    obj_type = [type(arg)]
    attrs = [attr for attr in dir(arg)]
    methods = [method for method, link in inspect.getmembers(arg) if callable(link)]
    obj_module = [inspect.getmodule(arg)]
    print (f'Тип объекта: {obj_type}')
    print (f'атрибуты объекта: {attrs}')
    print (f'методы объекта: {methods}')
    print (f'Обект находится в модуле: {obj_module}')

test = introspection_info(testobj)

