# Exercise 28: Define a class with default values.
class Dog:
def __init__(self, name="Fido"):
self.name = name

dog1 = Dog()
dog2 = Dog("Buddy")
print("Dog 1 name:", dog1.name)
print("Dog 2 name:", dog2.name)
