# Exercise 92: Check whether a class is a subclass of another.
class Animal:
pass

class Cat(Animal):
pass

print("Is Cat a subclass of Animal?", issubclass(Cat, Animal))
