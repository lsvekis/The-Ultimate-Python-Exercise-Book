# Exercise 81: Create a base class called Animal.
class Animal:
def __init__(self, name):
self.name = name

def speak(self):
return "Some sound"

a = Animal("Generic Animal")
print(a.name, "says", a.speak())
