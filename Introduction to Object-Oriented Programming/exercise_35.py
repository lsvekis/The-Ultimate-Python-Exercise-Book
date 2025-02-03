# Exercise 35: Use a class method as an alternative constructor.
class Person:
def __init__(self, name, age):
self.name = name
self.age = age

@classmethod
def from_string(cls, data_str):
name, age = data_str.split(",")
return cls(name.strip(), int(age.strip()))

p = Person.from_string("Quincy, 29")
print("Person from string:", p.name, p.age)
