# Exercise 4: Define a class with an initializer to set an attribute.
class Person:
def __init__(self, name):
self.name = name

p = Person("Alice")
print("Person's name:", p.name)
