# Exercise 96: Define a base class with a method that should be overridden.
class Shape:
def area(self):
raise NotImplementedError("Subclasses must implement area()")

class Circle(Shape):
def __init__(self, radius):
self.radius = radius

def area(self):
import math
return math.pi * (self.radius ** 2)

c = Circle(3)
print("Area of circle:", c.area())
