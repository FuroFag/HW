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
    obj_type_dict = {'Тип объекта': obj_type}
    attrs_dict = {'атрибуты объекта': attrs}
    methods_dict = {'методы объекта': methods}
    obj_module_dict = {'Обект находится в модуле': obj_module}
    
    return obj_type_dict, attrs_dict, methods_dict, obj_module_dict

test = introspection_info(testobj)

