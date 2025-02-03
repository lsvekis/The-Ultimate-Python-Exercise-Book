# Exercise 82: Define a Dog class that inherits from Animal.
class Animal:
def __init__(self, name):
self.name = name

def speak(self):
return "Some sound"

class Dog(Animal):
pass

d = Dog("Buddy")
print(d.name, "says", d.speak())
