# Exercise 14: Define __str__ to provide a readable representation.
class Person:
def __init__(self, name, age):
self.name = name
self.age = age

def __str__(self):
return f"{self.name} ({self.age} years old)"

p = Person("Frank", 40)
print("Person:", p)
