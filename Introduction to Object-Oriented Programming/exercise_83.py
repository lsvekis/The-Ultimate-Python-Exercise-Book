# Exercise 83: Override the speak() method in the Dog class.
class Animal:
def __init__(self, name):
self.name = name

def speak(self):
return "Some sound"

class Dog(Animal):
def speak(self):
return "Woof!"

d = Dog("Rex")
print(d.name, "says", d.speak())
