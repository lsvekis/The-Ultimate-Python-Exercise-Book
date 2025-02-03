# Exercise 84: Create a Cat class that inherits from Animal and overrides speak().
class Animal:
def __init__(self, name):
self.name = name

def speak(self):
return "Some sound"

class Cat(Animal):
def speak(self):
return "Meow!"

c = Cat("Whiskers")
print(c.name, "says", c.speak())
