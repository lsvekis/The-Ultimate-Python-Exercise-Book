# Exercise 87: Override __str__ in a subclass for custom string representation.
class Animal:
def __init__(self, name):
self.name = name

class Bird(Animal):
def __str__(self):
return f"Bird named {self.name}"

b = Bird("Tweety")
print(b)
