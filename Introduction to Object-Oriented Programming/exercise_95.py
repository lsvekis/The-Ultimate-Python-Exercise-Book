# Exercise 95: Use polymorphism by defining different speak() methods.
class Animal:
def speak(self):
return "Some sound"

class Dog(Animal):
def speak(self):
return "Woof!"

class Cat(Animal):
def speak(self):
return "Meow!"

def animal_sound(animal):
print(animal.speak())

animal_sound(Dog("Rex"))
animal_sound(Cat("Whiskers"))
