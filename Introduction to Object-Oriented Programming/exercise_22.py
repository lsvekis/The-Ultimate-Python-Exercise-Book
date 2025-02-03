# Exercise 22: Use the @property decorator to define a getter.
class Person:
def __init__(self, name):
self.__name = name

@property
def name(self):
return self.__name

p = Person("Ian")
print("Name using property:", p.name)
