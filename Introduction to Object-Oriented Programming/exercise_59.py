# Exercise 59: Distinguish between class and instance attributes.
class Animal:
species = "Mammal"  # Class attribute

def __init__(self, name):
self.name = name  # Instance attribute

dog = Animal("Buddy")
print("Dog name:", dog.name)
print("Dog species:", Animal.species)
