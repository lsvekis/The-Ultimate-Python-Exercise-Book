# Exercise 91: Check whether an object is an instance of a class.
class Animal:
pass

class Dog(Animal):
pass

d = Dog()
print("Is d an Animal?", isinstance(d, Animal))
