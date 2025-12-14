import inspect
import requests

print(inspect.ismodule(requests))
print(inspect.isclass(requests))
print(inspect.isfunction(requests))
print(inspect.getmodule(requests.get))
print(inspect.getmodule(list))

"""
data = "text"

def first_func():
    pass

print(callable(data))
print(callable(first_func))

class First_class:
    pass
class Second_class(First_class):
    pass

obj_2 = Second_class()

print(isinstance(obj_2, Second_class))
print(isinstance(obj_2, First_class))

print(issubclass(First_class, Second_class))
print(issubclass(Second_class, First_class))
"""

"""
print(hasattr(data, "reverse"))
print(hasattr(data, "index"))
print(hasattr(data, "startswith"))
print(getattr(data, "startswith"))
print(getattr(data, "reverse", None))
"""

"""
import requests

def first_function():
    pass
class Student:
    pass

rq = requests
first_f = first_function
Dmitriy = Student

print(requests.__name__)
print(rq.__name__)
print(first_function.__name__)
print(first_f.__name__)
print(Dmitriy.__name__)
print(Student.__name__)
print(__name__)
"""