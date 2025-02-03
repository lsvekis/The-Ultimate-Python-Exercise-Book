# Exercise 29: Define a class with a method that returns a greeting.
class Greeter:
def __init__(self, name):
self.name = name

def greet(self):
return f"Hi, {self.name}!"

g = Greeter("Lily")
print(g.greet())
