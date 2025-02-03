# Exercise 6: Define a method that uses the instance attribute.
class Person:
def __init__(self, name):
self.name = name

def greet(self):
print(f"Hello, my name is {self.name}.")

p = Person("Dave")
p.greet()
