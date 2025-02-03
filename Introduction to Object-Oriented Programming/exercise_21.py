# Exercise 21: Use methods to get and set a private attribute.
class Person:
def __init__(self, name):
self.__name = name

def get_name(self):
return self.__name

def set_name(self, name):
self.__name = name

p = Person("George")
print("Original name:", p.get_name())
p.set_name("Helen")
print("Updated name:", p.get_name())
