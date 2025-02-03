# Exercise 85: Use polymorphism by calling the same method on different subclasses.
class Animal:
def __init__(self, name):
self.name = name

def speak(self):
return "Some sound"

class Dog(Animal):
def speak(self):
return "Woof!"

class Cat(Animal):
def speak(self):
return "Meow!"

animals = [Dog("Fido"), Cat("Kitty"), Animal("Generic")]
for animal in animals:
print(animal.name, "says", animal.speak())
