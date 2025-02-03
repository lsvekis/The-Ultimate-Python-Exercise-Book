# Exercise 23: Define a property with both getter and setter.
class Person:
def __init__(self, name):
self.__name = name

@property
def name(self):
return self.__name

@name.setter
def name(self, new_name):
self.__name = new_name

p = Person("Jack")
print("Initial name:", p.name)
p.name = "Karen"
print("Changed name:", p.name)
